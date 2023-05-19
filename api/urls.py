from django.urls import path
from . import views

urlpatterns = [
 path('', views.getRoutes, name='routes'),
 path('notes/', views.getNotes, name="notes"),
 path('notes/<str:pk>', views.crudNote, name="crud-note"),
 path('todolists/', views.getToDoLists, name="todolists"),
]