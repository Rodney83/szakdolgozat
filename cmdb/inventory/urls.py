from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'', views.CiViewSet)
router.register(r'relations', views.CiRelationViewSet)

urlpatterns = router.urls
