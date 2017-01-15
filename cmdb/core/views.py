from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'inventory': reverse('configurationitem-list', request=request, format=format),
        'changes': reverse('change-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format),
        'taskstatus': reverse('taskstatus-list', request=request, format=format),
        'changestates': reverse('changestate-list', request=request, format=format),
        'closurecodes': reverse('closurecode-list', request=request, format=format),
    })

#TODO: create views for core serializers and add them to api root