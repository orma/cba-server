from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from .models import AdminUnit
from .serializers import AdminUnitSerializer


class ProvinceListView(generics.ListAPIView):
    queryset = AdminUnit.objects.get_provinces()
    serializer_class = AdminUnitSerializer
    renderer_classes = (JSONRenderer,)
    pagination_class = None