from django.conf.urls import url
from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'changes', views.ChangeViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'taskstatus', views.TaskStatusViewSet)
router.register(r'changestates', views.ChangeStateViewSet)
router.register(r'closurecodes', views.ClosureCodeViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^$', views.ChangeRootView.as_view(), name='change-root')
]