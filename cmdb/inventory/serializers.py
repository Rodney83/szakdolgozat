from rest_framework import serializers
import models


class ConfigurationItemSerializer(serializers.ModelSerializer):

    parents = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    class Meta:
        model = models.ConfigurationItem
        fields = "__all__"

    def get_parrents(self):
        return self.parent.all().values_list('parent_ci__logical_name', flat=True)

    def get_children(self):
        return self.children.all().values_list('child_ci__logical_name', flat=True)
