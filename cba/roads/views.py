from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from roads.models import Section
from roads.serializers import SectionSerializer


class SectionListView(generics.ListAPIView):
    queryset = Section.objects.order_by('-section_id', '-section_order')
    serializer_class = SectionSerializer
    renderer_classes = (JSONRenderer,)
