from django.db import models
from django.utils.translation import ugettext_lazy as _


class PropertyClass(models.Model):
    id = models.SmallIntegerField(_('id'), null=False, blank=False, primary_key=True)
    name = models.CharField(_('name'), null=False, blank=False, max_length=50)

    class Meta:
        abstract = True
        ordering = ('id',)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)


class ManagementClass(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('management class')
        verbose_name_plural = _('management classes')


class RoadClass(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('road class')
        verbose_name_plural = _('road classes')


class TerrainType(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('terrain type')
        verbose_name_plural = _('terrain types')


class TemperatureClass(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('temperature class')
        verbose_name_plural = _('temperature classes')


class MoistureClass(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('moisture class')
        verbose_name_plural = _('moisture classes')


class PavementType(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('pavement type')
        verbose_name_plural = _('pavement types')


class SurfaceType(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('surface type')
        verbose_name_plural = _('surface types')


class PavementConditionClass(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('pavement condition class')
        verbose_name_plural = _('pavement condition classes')


class TrafficLevel(PropertyClass):
    traffic_from = models.IntegerField(_('traffic from'), null=True, blank=True)
    traffic_to = models.IntegerField(_('traffic to'), null=True, blank=True)

    total_traffic = models.IntegerField(
        _('default total traffice (veh/day)'), null=True, blank=True
    )

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

    class Meta:
        ordering = ('id',)
        verbose_name = _('traffic levels')
        verbose_name_plural = _('traffic levels')


class TrafficGrowthScenario(PropertyClass):
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

    class Meta:
        ordering = ('id',)
        verbose_name = _('traffic annual growth scenario')
        verbose_name_plural = _('traffic annual growth scenarios')


class LaneClass(PropertyClass):
    from_width = models.FloatField(_('from width'), null=True, blank=True)
    to_width = models.FloatField(_('to width'), null=True, blank=True)
    number_of_lanes = models.SmallIntegerField(
        _('default number of lanes'), null=True, blank=True
    )
    carriageway_width = models.FloatField(
        _('default carriageway width'), null=True, blank=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = _('lanes class')
        verbose_name_plural = _('lanes classes')