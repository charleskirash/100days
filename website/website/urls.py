from django.contrib import admin
from projo import views
from django.urls import include, path

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
]
