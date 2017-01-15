from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'changes', views.ChangeListViewSet)
router.register(r'changes', views.ChangeDetailViewSet)
router.register(r'tasks', views.TaskListViewSet)
router.register(r'tasks', views.TaskDetailViewset)

urlpatterns = router.urls
