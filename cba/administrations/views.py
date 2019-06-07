from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from .models import AdminUnit
from .serializers import AdminUnitSerializer


class ProvinceListView(generics.ListAPIView):
    queryset = AdminUnit.objects.get_provinces()
    serializer_class = AdminUnitSerializer
    renderer_classes = (JSONRenderer,)


class ProvinceDetailView(generics.RetrieveAPIView):
    serializer_class = AdminUnitSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        try:
            return AdminUnit.objects.filter(
                pk=self.kwargs.get('pk'),
                type='province'
            )
        except AdminUnit.DoesNotExist:
            return None


class DistrictListView(generics.ListAPIView):
    serializer_class = AdminUnitSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        try:
            return AdminUnit.objects.filter(
                type='district',
                parent_id=self.kwargs.get('pk')
            ).order_by('id')
        except AdminUnit.DoesNotExist:
            return None
