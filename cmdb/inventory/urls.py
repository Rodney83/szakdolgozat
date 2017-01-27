from django.conf.urls import url
from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'configitem', views.CiViewSet)
router.register(r'relations', views.CiRelationViewSet)
router.register(r'cistatus', views.CiStatusViewSet)
router.register(r'citypes', views.CiTypeViewSet)
router.register(r'vendors', views.VendorsViewSet)
router.register(r'ipaddres', views.IpAddressViewSet)
router.register(r'companies', views.CompaniesViewSet)
router.register(r'cinetwork', views.CiNetworkNodeViewSet)
router.register(r'ciserver', views.CiServerNodeViewSet)
router.register(r'cios', views.CiOperatingSystemViewSet)
router.register(r'cimdlw', views.CiMiddlewareInstallationViewSet)
router.register(r'cimdlwinst', views.CiMiddlewareInstanceViewSet)
router.register(r'ciapps', views.CiApplicationViewSet)
router.register(r'cibusiness', views.CiBusinessContractViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^$', views.InventoryRootView.as_view(), name='inventory-root'),
]