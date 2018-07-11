from django.contrib import admin
from django.urls import path, include

from vocabulator.rest_api import views

app_name = "rest_api"

urlpatterns = [
    path('sync/', views.sync)
]
