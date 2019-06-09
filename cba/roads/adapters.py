from administrations.models import AdminUnit
from roads.constants import SECTION_FIELDS


class SectionCSVAdapter(object):
    def __init__(self, data=None):
        self._data = data
        self._instance = None

    def adapt(self, data=None):
        self._data = data if data else self._data

        self._instance = {}
        for field in SECTION_FIELDS:
            method = getattr(self, '_make_%s' % field, None)
            if method:
                self._instance[field] = method()

        return self._instance

    def makeFloatField(self, field_name, default=None):
        value = self._data.get(field_name, None)
        try:
            return float(value)
        except TypeError:
            return default

    def makeIntField(self, field_name, default=None):
        value = self._data.get(field_name, None)
        try:
            return int(value)
        except TypeError:
            return default

    def _make_section_id(self):
        return self._data.get('section_id', '')

    def _make_road_number(self):
        return self._data.get('road_number', '')

    def _make_road_name(self):
        return self._data.get('road_name', '')

    def _make_road_start(self):
        return self._data.get('road_start', '')

    def _make_road_end(self):
        return self._data.get('road_end', '')

    def _make_section_order(self):
        return self.makeIntField('section_order')

    def _make_province(self):
        """
        Take province name like 'Thanh Hoa' and resolves to pk of Province
        model
        """
        province = AdminUnit.objects.get_province_by_name(
            self._data.get('province', '')
        )
        if province is None:
            return None
        return province.id

    def _make_district(self):
        """
        Take district name like 'TT' and resolves to pk of Province
        model
        """
        district = AdminUnit.objects.get_district_by_name(
            self._data.get('district', '')
        )
        if district is None:
            return None
        return district.id

    def _make_commune(self):
        return self._data.get('commune', '')

    def _make_management(self):
        management = self._data.get('management', None)
        try:
            return int(management)
        except TypeError:
            return None

    def _make_start_km(self):
        return self.makeFloatField('start_km')

    def _make_end_km(self):
        return self.makeFloatField('end_km')
    
    def _make_length(self):
        return self.makeFloatField('length')

    def _make_lanes(self):
        return self.makeIntField('lanes')

    def _make_width(self):
        return self.makeFloatField('width')

    def _make_road_class(self):
        return self.makeIntField('road_class')

    def _make_terrain(self):
        return self.makeIntField('terrain')

    def _make_temperature(self):
        return self.makeIntField('temperature')

    def _make_moisture(self):
        return self.makeIntField('moisture')

    def _make_road_type(self):
        return self.makeIntField('road_type')

    def _make_surface_type(self):
        return self.makeIntField('surface_type')

    def _make_condition_class(self):
        return self.makeIntField('condition_class')

    def _make_roughness(self):
        return self.makeFloatField('roughness')

    def _make_traffic_level(self):
        return self.makeIntField('traffic_level')

    def _make_traffic_growth(self):
        return self.makeIntField('traffic_growth')

    def _make_pavement_age(self):
        return self.makeIntField('pavement_age')

    def _make_structural_no(self):
        return self.makeFloatField('structural_no')

    def _make_aadt_motorcyle(self):
        return self.makeFloatField('aadt_motorcyle')

    def _make_aadt_carsmall(self):
        return self.makeFloatField('aadt_carsmall')

    def _make_aadt_carmedium(self):
        return self.makeFloatField('aadt_carmedium')

    def _make_aadt_delivery(self):
        return self.makeFloatField('aadt_delivery')

    def _make_aadt_4wheel(self):
        return self.makeFloatField('aadt_4wheel')

    def _make_aadt_smalltruck(self):
        return self.makeFloatField('aadt_smalltruck')

    def _make_aadt_mediumtruck(self):
        return self.makeFloatField('aadt_mediumtruck')

    def _make_aadt_largetruck(self):
        return self.makeFloatField('aadt_largetruck')

    def _make_aadt_articulatedtruck(self):
        return self.makeFloatField('aadt_articulatedtruck')

    def _make_aadt_smallbus(self):
        return self.makeFloatField('aadt_smallbus')

    def _make_aadt_mediumbus(self):
        return self.makeFloatField('aadt_mediumbus')

    def _make_aadt_largebus(self):
        return self.makeFloatField('aadt_largebus')

    def _make_aadt_total(self):
        return self.makeFloatField('aadt_total')
