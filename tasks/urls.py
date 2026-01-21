from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("analyze/", views.analyze_tasks),
    path("suggest/", views.suggest_tasks),
]
