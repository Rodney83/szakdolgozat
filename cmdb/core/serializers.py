from rest_framework import serializers
import models


class UserProfileCiDetailSerializer(serializers.ModelSerializer):

    fullname = serializers.SerializerMethodField()

    class Meta:
        model = models.UserProfile
        fields = ('id', 'fullname', 'email')

    def get_fullname(self, instance):
        return instance.get_full_name()
