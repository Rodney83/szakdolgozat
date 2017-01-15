from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'', views.CiListViewSet)
router.register(r'', views.CiDetailViewSet)
router.register(r'relations', views.CiRelationViewSet)

urlpatterns = router.urls


#TODO: Create url routers for the misc. views