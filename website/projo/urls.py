from django.urls import path
from . import views

urlpatterns = [
    path("projo/", views.index, name="index"),
]
