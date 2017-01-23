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
router.register(r'cinetwork', views.CiNetworkNodeViewset)

urlpatterns = router.urls

urlpatterns += [
    url(r'^$', views.InventoryRootView.as_view(), name='inventory-root'),
]