from django.urls import path
from . import ClassBasedViews

urlpatterns = [
    path('', ClassBasedViews.index, name="list"),
    path('update_aufgabe/<str:pk>/',
         ClassBasedViews.updateAufgabe, name="update_aufgabe"),
    path('delete/<str:pk>/', ClassBasedViews.deleteAufgabe, name="delete"),
]
