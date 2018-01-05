from django.urls import path


from . import views

from .samples import static_json_example

urlpatterns = [
    path('', views.catalogue, name='cata'),
    path('listar', views.dato, name='listar'),
    path('static-json-example', static_json_example.chart, name='chart'),
]