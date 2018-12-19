"""
Utils to import administrative units from JSON file
"""
import json

from .serializers import AdminUnitSerializer
from .exceptions import InvalidProvinceData, InvalidDistrictData


def import_admin_unit(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    provinces = data['provinces']
    assert len(provinces) == 63, 'There should have 63 provinces. Please '\
        'check the province json file again'
    
    for province in provinces:
        districts = province.pop('districts', None)
        serializer = AdminUnitSerializer(data=province)
        
        if not serializer.is_valid():
            raise InvalidProvinceData(
                data=province, message=serializer.errors)

        pro_instance = serializer.save()

        for district in districts:
            serializer = AdminUnitSerializer(data=district)
            if not serializer.is_valid():
                raise InvalidDistrictData(
                    data=district, message=serializer.errors)
            
            serializer.save()
