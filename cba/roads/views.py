from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from roads.models import Section
from roads.serializers import BaseSectionSerializer


class SectionListView(generics.ListAPIView):
    queryset = Section.objects.order_by('-section_id', '-section_order')
    serializer_class = BaseSectionSerializer
    renderer_classes = (JSONRenderer,)
