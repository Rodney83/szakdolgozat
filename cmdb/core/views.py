from cmdb.prototypes import viewsets
import models
import serializers


class CoreRootView(viewsets.RootView):
    url_list = {
        'User Profiles': 'userprofile-list',
        'Manager Profiles': 'managerprofile-list',
        'Technical Groups': 'technicalgroups-list',
        'Management Groups': 'managementgroups-list',
    }


class UserProfileViewSet(viewsets.ListRetrieveViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileMinimalSerializer


class ManagerProfileViewSet(viewsets.ListRetrieveViewSet):
    queryset = models.ManagerProfile.objects.all()
    serializer_class = serializers.ManagerProfileMinimalSerializer


class TechnicalGroupViewSet(viewsets.ListRetrieveViewSet):
    queryset = models.TechnicalGroups.objects.all()
    serializer_class = serializers.TechnicalGroupsSerializer


class ManagementGroupViewSet(viewsets.ListRetrieveViewSet):
    queryset = models.ManagementGroups.objects.all()
    serializer_class = serializers.ManagementGroupsSerializer
