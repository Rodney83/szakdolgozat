from django.conf.urls import url
from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'managerprofiles', views.ManagerProfileViewSet)
router.register(r'technicalgroups', views.TechnicalGroupViewSet)
router.register(r'managementgroups', views.ManagementGroupViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^$', views.CoreRootView.as_view(), name='core-root')
]