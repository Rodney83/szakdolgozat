from rest_framework import mixins, viewsets, permissions


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


class ListViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Prototipus viewset a listazashoz
    """
    permission_classes = (permissions.DjangoModelPermissions, )

    class Meta:
        abstract = True


class CreateDestroyRetrieveUpdateViewSet(mixins.CreateModelMixin,
                                         mixins.RetrieveModelMixin,
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
    """
    permission_classes = (permissions.DjangoModelPermissions, )

    class Meta:
        abstract = True