from rest_framework import serializers
import models


class UserProfileMinimalSerializer(serializers.ModelSerializer):

    fullname = serializers.SerializerMethodField()

    class Meta:
        model = models.UserProfile
        fields = ('id', 'fullname', 'email')

    def get_fullname(self, instance):
        return instance.get_full_name()


class ManagerProfileMinimalSerializer(UserProfileMinimalSerializer):

    class Meta:
        model = models.ManagerProfile
        fields = UserProfileMinimalSerializer.Meta.fields


# TODO: Create serializers for the Groups