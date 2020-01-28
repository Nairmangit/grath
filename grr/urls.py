from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lk', views.lk, name = 'lk'),
    path('logg', views.logg, name = 'logg'),
    path('loggout', views.loggout, name = 'loggout'),
    path('grath', views.grath, name = 'grath'),
]
