from django.urls import path
from . import views

app_name='app'

urlpatterns = [
    path('', views.homepage),
    path('hola', views.hola, name="hola"),
]
