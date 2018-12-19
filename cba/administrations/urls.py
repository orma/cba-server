from django.urls import path

from . import views


app_name = 'administrations'

urlpatterns = [
    path('provinces/', view=views.ProvinceListView.as_view(), name='provinces'),
]