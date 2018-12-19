from django.db import models


class AdminUnitManager(models.Manager):
    def get_provinces(self):
        return self.filter(parent_id__isnull=True).order_by('name_en')
