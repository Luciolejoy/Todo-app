from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_aufgabe/<str:pk>/', views.updateAufgabe, name="update_aufgabe"),
    path('delete/<str:pk>/', views.deleteAufgabe, name="delete"),
]
