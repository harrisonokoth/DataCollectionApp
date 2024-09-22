from django.urls import path
from . import views
from .views import add_integration_config
urlpatterns = [
    path('', views.index, name='index'),
     path('add/', add_integration_config, name='add_integration_config'),
]
