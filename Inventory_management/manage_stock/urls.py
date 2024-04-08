from django.urls import path
from . import views

urlpatterns = [path("", views.bindex, name = "bindex")]