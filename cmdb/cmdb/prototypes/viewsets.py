from rest_framework import mixins, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.exceptions import ImproperlyConfigured


class RootView(APIView):

    url_list = dict()

    @classmethod
    def generate_urls(cls, request):
        if not cls.url_list:
            raise ImproperlyConfigured('url_list has to be defined')

        response = dict()
        for key, value in cls.url_list.items():
            response[key] = reverse(value, request=request)

        return response

    def get(self, request):
        response = self.__class__.generate_urls(request)
        return Response(response)


class CreateDestroyRetrieveViewSet(mixins.CreateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.DestroyModelMixin,
                                   viewsets.GenericViewSet):
    """
    Prototipus viewset a letrehozashoz, lekereshez es torleshez
    """
    permission_classes = (permissions.DjangoModelPermissions, )

    class Meta:
        abstract = True


class ListRetrieveViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """
    Prototipus viewset listazashoz es lekereshez
    """
    permission_classes = (permissions.DjangoModelPermissions, )

    class Meta:
        abstract = True


class CreateViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
        Prototipus viewset a listazashoz, letrehozashoz
        """
    permission_classes = (permissions.DjangoModelPermissions,)

    class Meta:
        abstract = True


class DestroyRetrieveUpdateViewSet(mixins.RetrieveModelMixin,
                                   mixins.DestroyModelMixin,
                                   mixins.UpdateModelMixin,
                                   viewsets.GenericViewSet):
    """
    Prototipus a letrehozsahoz, updateleshez, torleshez es lekereshez
    """
    permission_classes = (permissions.DjangoModelPermissions, )

    class Meta:
        abstract = True


class ModelViewSet(viewsets.ModelViewSet):
    """
    Default viewset ellatva alap hozzaferesi jogokhoz
    A serializer mappolassal megadhatok kulonbozo http keresekhez kulonbozo serializerek
    """
    permission_classes = (permissions.DjangoModelPermissions, )
    serializer_class = None
    serializer_map = {}

    def get_serializer_class(self):
        try:
            return self.serializer_map[self.action]
        except KeyError:
            return super(self.__class__, self).get_serializer_class()

    class Meta:
        abstract = True