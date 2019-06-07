from django.urls import path

from . import views


app_name = 'administrations'

urlpatterns = [
    path(
        'provinces/<int:pk>/districts/',
        view=views.DistrictListView.as_view(),
        name='districts'
    ),
    path(
        'provinces/<int:pk>/',
        view=views.ProvinceDetailView.as_view(),
        name='province-detail'
    ),
    path('provinces/', view=views.ProvinceListView.as_view(), name='provinces'),
]