import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from .managers import CBAResultManager


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
    truck_percent = models.FloatField(_('truck percent'), null=True, blank=True)
    vehicle_utilization = models.FloatField(
        _('vehicle utilization'), null=True, blank=True
    )
    esa_loading = models.FloatField(_('esa loading'), null=True, blank=True)

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

    objects = CBAResultManager()

    class Meta:
        verbose_name = _('cost benefit analysis result')


class TotalFinancialCost(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    province = models.ForeignKey(
        'administrations.AdminUnit', on_delete=models.SET_NULL, null=True
    )

    # Financial cost for 20 years
    work_cost_y1 = models.FloatField(_('work cost year 1'), null=True, blank=True)
    work_cost_y2 = models.FloatField(_('work cost year 2'), null=True, blank=True)
    work_cost_y3 = models.FloatField(_('work cost year 3'), null=True, blank=True)
    work_cost_y4 = models.FloatField(_('work cost year 4'), null=True, blank=True)
    work_cost_y5 = models.FloatField(_('work cost year 5'), null=True, blank=True)
    work_cost_y6 = models.FloatField(_('work cost year 6'), null=True, blank=True)
    work_cost_y7 = models.FloatField(_('work cost year 7'), null=True, blank=True)
    work_cost_y8 = models.FloatField(_('work cost year 8'), null=True, blank=True)
    work_cost_y9 = models.FloatField(_('work cost year 9'), null=True, blank=True)
    work_cost_y10 = models.FloatField(_('work cost year 10'), null=True, blank=True)
    work_cost_y11 = models.FloatField(_('work cost year 11'), null=True, blank=True)
    work_cost_y12 = models.FloatField(_('work cost year 12'), null=True, blank=True)
    work_cost_y13 = models.FloatField(_('work cost year 13'), null=True, blank=True)
    work_cost_y14 = models.FloatField(_('work cost year 14'), null=True, blank=True)
    work_cost_y15 = models.FloatField(_('work cost year 15'), null=True, blank=True)
    work_cost_y16 = models.FloatField(_('work cost year 16'), null=True, blank=True)
    work_cost_y17 = models.FloatField(_('work cost year 17'), null=True, blank=True)
    work_cost_y18 = models.FloatField(_('work cost year 18'), null=True, blank=True)
    work_cost_y19 = models.FloatField(_('work cost year 19'), null=True, blank=True)
    work_cost_y20 = models.FloatField(_('work cost year 20'), null=True, blank=True)
    work_cost_total = models.FloatField(_('work cost total'), null=True, blank=True)

    # npv for 20 years
    npv_y1 = models.FloatField(_('npv year 1'), null=True, blank=True)
    npv_y2 = models.FloatField(_('npv year 2'), null=True, blank=True)
    npv_y3 = models.FloatField(_('npv year 3'), null=True, blank=True)
    npv_y4 = models.FloatField(_('npv year 4'), null=True, blank=True)
    npv_y5 = models.FloatField(_('npv year 5'), null=True, blank=True)
    npv_y6 = models.FloatField(_('npv year 6'), null=True, blank=True)
    npv_y7 = models.FloatField(_('npv year 7'), null=True, blank=True)
    npv_y8 = models.FloatField(_('npv year 8'), null=True, blank=True)
    npv_y9 = models.FloatField(_('npv year 9'), null=True, blank=True)
    npv_y10 = models.FloatField(_('npv year 10'), null=True, blank=True)
    npv_y11 = models.FloatField(_('npv year 11'), null=True, blank=True)
    npv_y12 = models.FloatField(_('npv year 12'), null=True, blank=True)
    npv_y13 = models.FloatField(_('npv year 13'), null=True, blank=True)
    npv_y14 = models.FloatField(_('npv year 14'), null=True, blank=True)
    npv_y15 = models.FloatField(_('npv year 15'), null=True, blank=True)
    npv_y16 = models.FloatField(_('npv year 16'), null=True, blank=True)
    npv_y17 = models.FloatField(_('npv year 17'), null=True, blank=True)
    npv_y18 = models.FloatField(_('npv year 18'), null=True, blank=True)
    npv_y19 = models.FloatField(_('npv year 19'), null=True, blank=True)
    npv_y20 = models.FloatField(_('npv year 20'), null=True, blank=True)
    npv_total = models.FloatField(_('npv total'), null=True, blank=True)

    class Meta:
        verbose_name = _('Total Financial Cost')


class BudgetScenario(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)

    province = models.ForeignKey(
        'administrations.AdminUnit', on_delete=models.SET_NULL, null=True
    )

    # 3 years rolling or 5 years rolling
    program = models.SmallIntegerField(
        _('rolling program'), null=True, blank=True, default=3)
    
    budget_percent = models.FloatField(
        _('budget percentage'), null=True, blank=True, default=100.0
    )
    total_capital = models.FloatField(
        _('total capital cost'), null=True, blank=True
    )

    periodic_maintenance_cost = models.FloatField(
        _('period maintenance cost'), null=True, blank=True
    )
    rehabilitation_financial_cost = models.FloatField(
        _('Rehabilitation Financial Cost'), null=True, blank=True
    )
    recurrent_cost = models.FloatField(
        _('recurrent cost'), null=True, blank=True
    )
    total_agency_cost = models.FloatField(
        _('Total Capital Cost'), null=True, blank=True
    )
    periodic_maintenance_road_works = models.FloatField(
        _('Periodic Maintenance Road Works'), null=True, blank=True
    )
    rehabilitation_road_works = models.FloatField(
        _('Rehabilitation Road Works'), null=True, blank=True
    )
    total_capital_road_works = models.FloatField(
        _('Total Capital Road Works'), null=True, blank=True
    )
    total_recurrent_road_works = models.FloatField(
        _('Total Capital Road Works'), null=True, blank=True
    )

    no_prioritised_sections = models.SmallIntegerField(
        _('number of selected priority road sections'), null=True, blank=True
    )
    npv = models.FloatField(_('npv'), null=True, blank=True)

    class Meta:
        verbose_name = _('budget scenario')