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
    class Meta:
        ordering = ('id',)
        verbose_name = _('traffic levels')
        verbose_name_plural = _('traffic levels')


class TrafficGrowthScenario(PropertyClass):
    class Meta:
        ordering = ('id',)
        verbose_name = _('traffic annual growth scenario')
        verbose_name_plural = _('traffic annual growth scenarios')
