from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from projo import views

urlpatterns = [
    path("projo/", views.SnippetList.as_view()),
    path("projo/<int:pk>/", views.SnippetDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

