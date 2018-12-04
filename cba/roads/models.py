from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Section(TimeStampedModel):
    road_section_id = models.CharField(
        _('road section id'), max_length=30, null=False, primary_key=True)
    road_number = models.SmallIntegerField(_('road number'), null=False)
    road_name = models.CharField(_('road name'), max_length=255, blank=False)
    road_start = models.CharField(
        _('road start'), max_length=255, blank=False, null=True)
    road_end = models.CharField(
        _('road end'), max_length=255, blank=False, null=True)

    section_order = models.SmallIntegerField(_('section order'), null=True)
    section_name = models.CharField(
        _('section name'), max_length=255, blank=False, null=True)

    class Meta:
        ordering = ('road_section_id',)
        verbose_name = _('section')
        verbose_name_plural = _('sections')

    def __str__(self):
        return self.road_section_id
