from django.db import models


class CBAResultManager(models.Manager):
    def get_results_for_province(self, province):
        return self.filter(section__province=province)

    def get_results_by_province_name(self, province_name):
        return self.filter(section__province__name_en__iexact=province_name)