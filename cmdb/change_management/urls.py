from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'changes', views.ChangeListViewSet)
router.register(r'changes', views.ChangeDetailViewSet)
router.register(r'tasks', views.TaskListViewSet)
router.register(r'tasks', views.TaskDetailViewset)
router.register(r'taskstatus', views.TaskStatusViewSet)
router.register(r'changestates', views.ChangeStateViewSet)
router.register(r'closurecodes', views.ClosureCodeViewSet)

urlpatterns = router.urls
