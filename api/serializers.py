
from rest_framework.serializers import ModelSerializer
from . models import *
from collab_app.models import ToDoList

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class ToDoListSerializer(ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'