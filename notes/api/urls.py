from django.urls import path
from . import views

urlpatterns = [
    path('', views.getroutes, name='routes'),
    path('notes/', views.getnotes, name='notes'),
    path('notes/<str:pk>/', views.getnote, name='note'),
    path('notes/<str:pk>/update/', views.updateNote, name='update-note'),
    path('notes/<str:pk>/delete/', views.deleteNote, name='delete-note'),
    path('notes/create', views.createNote, name='create-note'),
]
