from rest_framework import serializers
import models
import core.serializers


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


class ConfigurationItemSerializer(ConfigurationItemMinimalSerializer):

    status = serializers.SlugRelatedField(slug_field='name', queryset=models.CiStatus.objects.all())
    ci_type = serializers.SlugRelatedField(slug_field='name', queryset=models.CiType.objects.all())
    engineering_group = serializers.SlugRelatedField(slug_field='name', queryset=models.TechnicalGroups.objects.all())
    administrator_groups = serializers.SlugRelatedField(slug_field='name', many=True,
                                                        queryset=models.TechnicalGroups.objects.all())
    responsible = core.serializers.UserProfileMinimalSerializer(read_only=True)
    parents = CiRelationParentSerializer(many=True)
    children = CiRelationChildSerializer(read_only=True, many=True)

    class Meta(ConfigurationItemMinimalSerializer.Meta):
        model = ConfigurationItemMinimalSerializer.Meta.model
        fields = ConfigurationItemMinimalSerializer.Meta.fields + \
                 ('verbose_name',
                  'status',
                  'ci_type',
                  'last_mod_time',
                  'engineering_group',
                  'administrator_groups',
                  'responsible',
                  'parents',
                  'children')

    def create(self, validated_data):
        # TODO: Implement code for storing responsible too
        validated_data.pop('logical_name')
        admin_groups = validated_data.pop('administrator_groups')
        parents = validated_data.pop('parents')
        obj = validated_data.get('ci_type', None)
        if obj:
            first_part = obj.name.upper()
        else:
            first_part = 'UNDEFINED'

        try:
            second_part = models.ConfigurationItem.objects.latest('id').id + 1
        except models.ConfigurationItem.DoesNotExist:
            second_part = 1
        logical_name = first_part + str(second_part)
        instance = models.ConfigurationItem.objects.create(logical_name=logical_name, **validated_data)
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
        # TODO: Implement code for storing responsible too
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


