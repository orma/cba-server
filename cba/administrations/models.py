from django.db import models
from django.utils.translation import ugettext_lazy as _


class AdminUnit(models.Model):
    id = models.IntegerField(_('id'), null=False, blank=False, primary_key=True)
    code = models.CharField(_('code'), null=True, blank=True, max_length=10)
    parent_id = models.IntegerField(_('parent id'), null=True, blank=True)
    name_en = models.CharField(_('name in English'), null=True, blank=True, max_length=100)
    name_vn = models.CharField(_('name in Vietnamese'), null=True, blank=True, max_length=100)
    type = models.CharField(_('type'), null=False, blank=False, max_length=20)
    total = models.FloatField(_('total'), null=True, blank=True)
    vpromm = models.FloatField(_('vpromm'), null=True, blank=True)

    class Meta:
        verbose_name = _('administrative unit')
        verbose_name_plural = _('administrative units')
    
    def __str__(self):
        return "{} - {}".format(self.id, self.name_en)
