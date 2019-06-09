from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from .property_classes import *


class Section(TimeStampedModel):
    orma_way_id = models.IntegerField(
        _('orma way id'), blank=True, null=True)
    vpromm_id = models.CharField(
        _('vpromm id'), blank=True, null=True, max_length=20)
    section_id = models.CharField(
        _('section id'), max_length=30, null=False, primary_key=True)
    road_number = models.CharField(
        _('road number'), max_length=10, null=True, blank=True)
    road_name = models.CharField(_('road name'), max_length=255, blank=False)
    road_start = models.CharField(
        _('road start'), max_length=255, blank=False, null=True)
    road_end = models.CharField(
        _('road end'), max_length=255, blank=False, null=True)

    section_order = models.SmallIntegerField(_('section order'), null=True)
    
    province = models.ForeignKey('administrations.AdminUnit', null=True,
                                  blank=True, on_delete=models.PROTECT,
                                  related_name='province_sections')
    district = models.ForeignKey('administrations.AdminUnit', null=True,
                                 blank=True, on_delete=models.PROTECT,
                                 related_name='district_sections')

    commune = models.CharField(_('commune'), max_length=25, null=True, blank=True)
    management = models.SmallIntegerField(_('management'), null=True, blank=True)

    start_km = models.FloatField(_('start km'), null=True, blank=True)
    end_km = models.FloatField(_('end km'), null=True, blank=True)
    length = models.FloatField(_('length'), null=False, blank=False, default=0.0)
    lanes = models.SmallIntegerField(_('number of lanes class'), null=True, blank=True)
    width = models.FloatField(_('carriageway width'), null=True, blank=True)
    road_class = models.SmallIntegerField(_('road class'), null=True, blank=True)
    terrain = models.SmallIntegerField(_('terrain type'), null=True, blank=True)
    temperature = models.SmallIntegerField(_('temperature class'), null=True, blank=True)
    moisture = models.SmallIntegerField(_('moisture class'), null=True, blank=True)
    road_type = models.SmallIntegerField(_('pavement type'), null=True, blank=True)
    surface_type = models.SmallIntegerField(_('surface type'), null=True, blank=True)
    condition_class = models.SmallIntegerField(_('pavement condition class'), null=True, blank=True)
    roughness = models.FloatField(_('roughness (IRI)'), null=True, blank=True)
    traffic_level = models.SmallIntegerField(_('traffic level'), null=True, blank=True)
    traffic_growth = models.SmallIntegerField(_('traffic annual growth scenario'), null=True, blank=True)
    structural_no = models.FloatField(_('structural number'), null=True, blank=True)
    pavement_age = models.SmallIntegerField(_('pavement age'), null=True, blank=True)

    aadt_motorcyle = models.FloatField(_('aadt_motorcyle'), null=True, blank=True)
    aadt_carsmall = models.FloatField(_('aadt_carsmall'), null=True, blank=True)
    aadt_carmedium = models.FloatField(_('aadt_carmedium'), null=True, blank=True)
    aadt_delivery = models.FloatField(_('aadt_delivery'), null=True, blank=True)
    aadt_4wheel = models.FloatField(_('aadt_4wheel'), null=True, blank=True)
    aadt_smalltruck = models.FloatField(_('aadt_smalltruck'), null=True, blank=True)
    aadt_mediumtruck = models.FloatField(_('aadt_mediumtruck'), null=True, blank=True)
    aadt_largetruck = models.FloatField(_('aadt_largetruck'), null=True, blank=True)
    aadt_articulatedtruck = models.FloatField(_('aadt_articulatedtruck'), null=True, blank=True)
    aadt_smallbus = models.FloatField(_('aadt_smallbus'), null=True, blank=True)
    aadt_mediumbus = models.FloatField(_('aadt_mediumbus'), null=True, blank=True)
    aadt_largebus = models.FloatField(_('aadt_largebus'), null=True, blank=True)
    aadt_total = models.FloatField(_('aadt_total'), null=True, blank=True)

    class Meta:
        ordering = ('section_id',)
        verbose_name = _('section')
        verbose_name_plural = _('sections')

    def __str__(self):
        return self.section_id
