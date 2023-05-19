
from rest_framework.serializers import ModelSerializer
from . models import *
from collab_app.models import ToDoList, ToDoItem

class ToDoListSerializer(ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'

class ToDoItemSerializer(ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'