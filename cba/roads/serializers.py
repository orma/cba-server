from rest_framework import serializers

from .models import Section
from .property_classes import (
    ManagementClass, TerrainType, TemperatureClass, LaneClass, RoadClass,
    MoistureClass, PavementType, PavementConditionClass, SurfaceType,
    TrafficLevel, TrafficGrowthScenario
)


class BaseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    """
    This serializer is used to get section information that can be displayed
    in most of the frontend
    """
    road_section_id = serializers.CharField(source='section_id')

    section_name = serializers.SerializerMethodField()
    def get_section_name(self, section):
        """Currently no data for this attribute"""
        return None

    province = serializers.SerializerMethodField()
    def get_province(self, section):
        try:
            return section.province.name_en
        except:
            return None

    district = serializers.SerializerMethodField()
    def get_district(self, section):
        try:
            return section.district.code
        except:
            return None

    management = serializers.SerializerMethodField()
    def get_management(self, section):
        try:
            mc = ManagementClass.objects.get(pk=section.management)
            return "{}: {}".format(mc.id, mc.name)
        except ManagementClass.DoesNotExist:
            return None

    terrain_type = serializers.SerializerMethodField()
    def get_terrain_type(self, section):
        try:
            tt = TerrainType.objects.get(pk=section.terrain)
            return "{}: {}".format(tt.id, tt.name)
        except TerrainType.DoesNotExist:
            return None

    temperature_class = serializers.SerializerMethodField()
    def get_temperature_class(self, section):
        try:
            tt = TemperatureClass.objects.get(pk=section.temperature)
            return "{}: {}".format(tt.id, tt.name)
        except TemperatureClass.DoesNotExist:
            return None

    lanes = serializers.SerializerMethodField()
    def get_lanes(self, section):
        try:
            lc = LaneClass.objects.get(pk=section.lanes)
            return "{}: {}".format(lc.id, lc.name)
        except LaneClass.DoesNotExist:
            return None

    road_class = serializers.SerializerMethodField()
    def get_road_class(self, section):
        try:
            rc = RoadClass.objects.get(pk=section.road_class)
            return "{}: {}".format(rc.id, rc.name)
        except RoadClass.DoesNotExist:
            return None

    moisture_class = serializers.SerializerMethodField()
    def get_moisture_class(self, section):
        try:
            mc = MoistureClass.objects.get(pk=section.moisture)
            return "{}: {}".format(mc.id, mc.name)
        except MoistureClass.DoesNotExist:
            return None

    pavement_type = serializers.SerializerMethodField()
    def get_pavement_type(self, section):
        try:
            pt = PavementType.objects.get(pk=section.road_type)
            return "{}: {}".format(pt.id, pt.name)
        except PavementType.DoesNotExist:
            return None

    pavement_condition_class = serializers.SerializerMethodField()
    def get_pavement_condition_class(self, section):
        try:
            pcc = PavementConditionClass.objects.get(pk=section.condition_class)
            return "{}: {}".format(pcc.id, pcc.name)
        except PavementConditionClass.DoesNotExist:
            return None

    surface_type = serializers.SerializerMethodField()
    def get_surface_type(self, section):
        try:
            st = SurfaceType.objects.get(pk=section.surface_type)
            return "{}: {}".format(st.id, st.name)
        except SurfaceType.DoesNotExist:
            return None

    traffic_level = serializers.SerializerMethodField()
    def get_traffic_level(self, section):
        try:
            tl = TrafficLevel.objects.get(pk=section.traffic_level)
            return "{}: {}".format(tl.id, tl.name)
        except TrafficLevel.DoesNotExist:
            return None

    traffic_growth = serializers.SerializerMethodField()
    def get_traffic_growth(self, section):
        try:
            qs = TrafficGrowthScenario.objects.get(pk=section.traffic_growth)
            return "{}: {}".format(qs.id, qs.name)
        except TrafficGrowthScenario.DoesNotExist:
            return None

    class Meta:
        model = Section
        fields = (
            'road_section_id', 'road_number', 'road_name', 'road_start',
            'road_end', 'section_order', 'section_name', 'province', 'district',
            'commune', 'management', 'start_km', 'end_km', 'length', 'lanes',
            'width', 'road_class', 'terrain_type', 'temperature_class',
            'moisture_class', 'pavement_type', 'pavement_condition_class',
            'surface_type', 'roughness', 'structural_no', 'pavement_age',
            'traffic_level', 'traffic_growth', 'aadt_motorcyle',
            'aadt_carsmall', 'aadt_carmedium', 'aadt_delivery', 'aadt_4wheel',
            'aadt_smalltruck', 'aadt_mediumtruck', 'aadt_largetruck',
            'aadt_articulatedtruck', 'aadt_smallbus', 'aadt_mediumbus',
            'aadt_largebus', 'aadt_total',
        )