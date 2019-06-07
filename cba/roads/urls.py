from django.urls import path

from . import views


app_name = 'road'

urlpatterns = [
    path('sections/', view=views.SectionListView.as_view(), name='sections'),
]