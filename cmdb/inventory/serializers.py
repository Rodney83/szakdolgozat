from rest_framework import serializers
from django.db.models import Max
import models


class CiStatusSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.CiStatus
        fields = ('id', 'name')


class CiTypeSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.CiType
        fields = ('id', 'name')


class VendorsSerializerMinimal(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Vendors
        fields = ('id', 'name')


class VendorsSerializer(VendorsSerializerMinimal):

    class Meta:
        model = VendorsSerializerMinimal.Meta.model
        fields = VendorsSerializerMinimal.Meta.fields + (
            'url', 'contact_email', 'contact_phone'
        )


class IpAddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.IpAddress
        fields = ('url', 'id', 'ip', 'fqdn')


class CompaniesMinimalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Companies
        fields = ('id', 'name')


class CompaniesSerializer(CompaniesMinimalSerializer):

    class Meta:
        model = CompaniesMinimalSerializer.Meta.model
        fields = CompaniesMinimalSerializer.Meta.fields + (
            'url', 'contact_name', 'contact_email', 'contact_email'
        )


class ConfigurationItemMinimalSerializer(serializers.HyperlinkedModelSerializer):
    logical_name = serializers.CharField()

    class Meta:
        model = models.ConfigurationItem
        fields = ('url', 'logical_name',)


class CiRelationSerializer(serializers.HyperlinkedModelSerializer):
    relation = serializers.SerializerMethodField()

    class Meta:
        model = models.CiRelation
        fields = ('url', 'relation')

    def get_relation(self, instance):
        return instance.__str__()


class CiRelationParentSerializer(serializers.HyperlinkedModelSerializer):
    parent_ci = ConfigurationItemMinimalSerializer()

    class Meta:
        model = models.CiRelation
        fields = ('url', 'parent_ci')


class CiRelationChildSerializer(serializers.HyperlinkedModelSerializer):
    child_ci = ConfigurationItemMinimalSerializer(read_only=True)

    class Meta:
        model = models.CiRelation
        fields = ('url', 'child_ci')


class ConfigurationItemListSerializer(ConfigurationItemMinimalSerializer):
    logical_name = serializers.CharField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='name', queryset=models.CiStatus.objects.all())
    ci_type = serializers.SlugRelatedField(slug_field='name', queryset=models.CiType.objects.all())
    engineering_group = serializers.SlugRelatedField(slug_field='name', queryset=models.TechnicalGroups.objects.all())

    class Meta:
        model = ConfigurationItemMinimalSerializer.Meta.model
        fields = ConfigurationItemMinimalSerializer.Meta.fields + (
            'verbose_name',
            'status',
            'ci_type',
            'engineering_group',
        )


class ConfigurationItemDetailSerializer(ConfigurationItemListSerializer):

    administrator_groups = serializers.SlugRelatedField(slug_field='name', many=True,
                                                        queryset=models.TechnicalGroups.objects.all())
    responsible = serializers.SlugRelatedField(slug_field='email', queryset=models.UserProfile.objects.all())
    parents = CiRelationParentSerializer(many=True)
    children = CiRelationChildSerializer(read_only=True, many=True)

    class Meta:
        model = ConfigurationItemListSerializer.Meta.model
        fields = ConfigurationItemListSerializer.Meta.fields + \
                 (
                  'last_mod_time',
                  'administrator_groups',
                  'responsible',
                  'parents',
                  'children')

    def create(self, validated_data):
        admin_groups = validated_data.pop('administrator_groups')
        parents = validated_data.pop('parents')
        ci_type = validated_data.get('ci_type', None)

        if ci_type:
            first_part = ci_type.name.upper()
        else:
            first_part = 'UNDEFINED'

        second_part = models.ConfigurationItem.objects.aggregate(Max('id'))['id__max'] + 1
        logical_name = first_part + str(second_part).zfill(5)
        instance = self.Meta.model.objects.create(logical_name=logical_name, **validated_data)
        instance.administrator_groups.add(*admin_groups)
        for item in parents:
            try:
                ci = models.ConfigurationItem.objects.get(logical_name=item['parent_ci']['logical_name'])
            except models.ConfigurationItem.DoesNotExist:
                print ('Given parent Ci does not exist')
            else:
                models.CiRelation.objects.create(parent_ci=ci, child_ci=instance)

        return instance

    def update(self, instance, validated_data):
        instance.verbose_name = validated_data.get('verbose_name', instance.verbose_name)
        instance.status = validated_data.get('status', instance.status)
        instance.engineering_group = validated_data.get('engineering_group', instance.engineering_group)
        admin_groups = validated_data.get('administrator_groups', [])
        instance.administrator_groups.clear()
        instance.administrator_groups.add(*admin_groups)
        instance.responsible = validated_data.get('responsible', None)
        instance.save()

        existing_parents = list(instance.parents.all().values_list('parent_ci__logical_name', flat=True))
        new_parents = validated_data.get('parents', [])

        for item in new_parents:
            try:
                ci = models.ConfigurationItem.objects.get(logical_name=item['parent_ci']['logical_name'])
            except models.ConfigurationItem.DoesNotExist:
                print ('Given parent Ci does not exist')
            else:
                models.CiRelation.objects.get_or_create(parent_ci=ci, child_ci=instance)
                if ci.logical_name in existing_parents:
                    existing_parents.remove(ci.logical_name)

        for item in existing_parents:
            models.CiRelation.objects.get(parent_ci__logical_name=item).delete()

        return instance


class CiNetworkNodeListSerializer(ConfigurationItemListSerializer):

    class Meta:
        model = models.CiNetworkNode
        fields = ConfigurationItemListSerializer.Meta.fields


class CiNetworkNodeDetailSerializer(ConfigurationItemDetailSerializer):

    hardware_vendor = serializers.SlugRelatedField(slug_field='name', queryset=models.Vendors.objects.all())
    ip_addresses = serializers.SlugRelatedField(slug_field='ip', queryset=models.IpAddress.objects.all(), many=True)

    class Meta:
        model = models.CiNetworkNode
        fields = ConfigurationItemDetailSerializer.Meta.fields + (
            'hardware_vendor',
            'number_of_ports',
            'ip_addresses'
        )

    def create(self, validated_data):
        ip = validated_data.pop('ip_addresses')
        instance = super(CiNetworkNodeDetailSerializer, self).create(validated_data)
        instance.ip_addresses.add(*ip)
        return instance

    def update(self, instance, validated_data):
        instance.hardware_vendor = validated_data.get('hardware_vendor', instance.hardware_vendor)
        instance.number_of_ports = validated_data.get('number_of_ports', instance.number_of_ports)
        ip = validated_data.get('ip_addresses', [])
        instance.ip_addresses.clear()
        instance.ip_addresses.add(*ip)
        return super(CiNetworkNodeDetailSerializer, self).update(validated_data)
