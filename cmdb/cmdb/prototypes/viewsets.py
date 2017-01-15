from rest_framework import mixins, viewsets, permissions


class CreateDestroyViewset(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    """
    Prototipus viewset a letrehozashoz, lekereshez es torleshez
    """
    permission_classes = (permissions.DjangoModelPermissions, )
    class Meta:
        abstract = True


class ModelViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    class Meta:
        abstract = True