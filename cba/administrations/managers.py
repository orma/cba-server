from django.db import models


class AdminUnitManager(models.Manager):
    def get_provinces(self):
        return self.filter(parent_id__isnull=True).order_by('name_en')

    def get_province_by_name(self, name):
        return self.filter(name_en__iexact=name, type='province').first()

    def get_district_by_name(self, name):
        return self.filter(code__iexact=name, type='district').first()
