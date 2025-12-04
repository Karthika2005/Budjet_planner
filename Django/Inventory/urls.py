from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_planner, name='budget_planner'),
]
