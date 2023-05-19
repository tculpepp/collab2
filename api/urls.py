from django.urls import path
from . import views

urlpatterns = [
 path('todolists/', views.getToDoLists, name="todolists"),
 path('todoitems/', views.getToDoItem, name="todoitems"),
]