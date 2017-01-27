from cmdb.prototypes import viewsets
import models
import serializers


class InventoryRootView(viewsets.RootView):
    url_list = {
        'Configuration Items': 'configurationitem-list',
        'Network Noeds': 'cinetworknode-list',
        'Ci Status': 'cistatus-list',
        'Ci Types': 'citype-list',
        'Vendors': 'vendors-list',
        'IP Address': 'ipaddress-list',
        'Companies': 'companies-list',
    }


class CiViewSet(viewsets.ModelViewSet):
    queryset = models.ConfigurationItem.objects.all()
    serializer_class = serializers.ConfigurationItemDetailSerializer
    serializer_map = {
        'list': serializers.ConfigurationItemListSerializer
    }


class CiNetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = models.CiNetworkNode.objects.all()
    serializer_class = serializers.CiNetworkNodeDetailSerializer
    serializer_map = {
        'list': serializers.CiNetworkNodeListSerializer
    }


class CiServerNodeViewSet(viewsets.ModelViewSet):
    queryset = models.CiServerNode.objects.all()
    serializer_class = serializers.CiServerNodeDetailSerializer
    serializer_map = {
        'list': serializers.CiNetworkNodeListSerializer
    }


class CiOperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = models.CiOperatingSystem.objects.all()
    serializer_class = serializers.CiOperatingSystemDetailSerializer
    serializer_map = {
        'list': serializers.CiOperatingSystemListSerializer
    }


class CiMiddlewareInstallationViewSet(viewsets.ModelViewSet):
    queryset = models.CiMiddlewareInstallation.objects.all()
    serializer_class = serializers.CiMiddlewareInstallationDetailSerializer
    serializer_map = {
        'list': serializers.CiMiddlewareInstallationListSerializer
    }


class CiMiddlewareInstanceViewSet(viewsets.ModelViewSet):
    queryset = models.CiMiddlewareInstance.objects.all()
    serializer_class = serializers.CiMiddlewareInstanceDetailSerializer
    serializer_map = {
        'list': serializers.CiMiddlewareInstanceListSerializer
    }


class CiApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.CiApplication.objects.all()
    serializer_class = serializers.CiApplicationDetailSerializer
    serializer_map = {
        'list': serializers.CiApplicationDetailSerializer
    }


class CiBusinessContractViewSet(viewsets.ModelViewSet):
    queryset = models.CiBusinessContract.objects.all()
    serializer_class = serializers.CiBusinessContractDetailSerializer
    serializer_map = {
        'list': serializers.CiBusinessContractListSerializer
    }


class CiRelationViewSet(viewsets.CreateDestroyRetrieveViewSet):
    queryset = models.CiRelation.objects.all()
    serializer_class = serializers.CiRelationSerializer


class CiStatusViewSet(viewsets.ModelViewSet):
    queryset = models.CiStatus.objects.all()
    serializer_class = serializers.CiStatusSerializer


class CiTypeViewSet(viewsets.ModelViewSet):
    queryset = models.CiType.objects.all()
    serializer_class = serializers.CiTypeSerializer


class VendorsViewSet(viewsets.ModelViewSet):
    queryset = models.Vendors.objects.all()
    serializer_class = serializers.VendorsSerializer
    serializer_map = {
        'list': serializers.VendorsSerializerMinimal
    }


class IpAddressViewSet(viewsets.ModelViewSet):
    queryset = models.IpAddress.objects.all()
    serializer_class = serializers.IpAddressSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = models.Companies.objects.all()
    serializer_class = serializers.CompaniesMinimalSerializer
    serializer_map = {
        'list': serializers.CompaniesMinimalSerializer
    }


