import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class CBAResult(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)

    # Recommended Road Work
    work_class = models.CharField(_('work class'), max_length=100, blank=True)
    work_type = models.CharField(_('work type'), max_length=100, blank=True)
    work_name = models.CharField(_('work name'), max_length=100, blank=True)
    work_cost = models.FloatField(_('financial cost'), null=True, blank=True)
    work_cost_km = models.FloatField(
        _('financial cost per km'), null=True, blank=True
    )
    work_year = models.SmallIntegerField(
        _('implementation year'), null=True, blank=True
    )

    # Economic Indicators
    npv = models.FloatField(_('npv'), null=True, blank=True)
    npv_km = models.FloatField(_('npv per km'), null=True, blank=True)
    npv_cost = models.FloatField(
        _('npv per road work cost'), null=True, blank=True
    )
    eirr = models.FloatField(_('eirr'), null=True, blank=True)

    # Total traffic vehicle per day (in 10 years)
    aadt = ArrayField(
        models.FloatField(null=True, blank=True), size=10
    )

    # Roughness Project Alternative (IRI, m/km) (in 10 years)
    iri_projection = ArrayField(
        models.FloatField(null=True, blank=True), size=10
    )

    # Roughness Base Alternative (IRI, m/km)
    iri_base = ArrayField(
        models.FloatField(null=True, blank=True), size=10
    )

    # Pavement Condition Class Project Alternative (1 to 5)
    con_projection = ArrayField(
        models.SmallIntegerField(null=True, blank=True), size=10
    )

    # Pavement Condition Class Base Alternative (1 to 5) (in 10 years)
    con_base = ArrayField(
        models.SmallIntegerField(null=True, blank=True), size=10
    )

    # Financial Recurrent Costs ($ Million) (in 10 years)
    financial_recurrent_cost = ArrayField(
        models.FloatField(null=True, blank=True), size=10
    )

    # Net Benefits ($ Million) (in 20 years)
    net_benefits = ArrayField(
        models.FloatField(null=True, blank=True), size=20
    )

    section = models.ForeignKey(
        'roads.Section', on_delete=models.CASCADE, related_name='cba_results'
    )

    class Meta:
        verbose_name = _('cost benefit analysis result')
