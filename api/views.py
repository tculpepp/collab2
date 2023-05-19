from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *
from collab_app.models import ToDoList, ToDoItem

@api_view(['GET'])
def getRoutes(request):

	routes = [  
		{  
		'Endpoint': '/notes/',  
		'method': 'GET',  
		'body': None,  
		'description': 'Returns an array of notes'  
		},  
		{  
		'Endpoint': '/notes/',  
		'method': 'POST',  
		'body': {'body': ""},  
		'description': 'Creates new note with data sent in post request'  
		},  
		{  
		'Endpoint': '/notes/id/',  
		'method': 'GET',  
		'body': None,  
		'description': 'Returns a single note object'  
		},  
		{  
		'Endpoint': '/notes/id/',  
		'method': 'PUT',  
		'body': {'body': ""},  
		'description': 'Creates an existing note with data sent in post request'  
		},  
		{  
		'Endpoint': '/notes/id/',  
		'method': 'DELETE',  
		'body': None,  
		'description': 'Deletes an existing note'  
		},  
	]
	return Response(routes)

@api_view(['GET', 'POST'])
def getNotes(request):
    if (request.method == 'GET'):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    elif (request.method == 'POST'): # add conditional
        data = request.data # grab data from user
        note = Note.objects.create(body=data['body']) # create new note with body property
        serializer = NoteSerializer(note, many=False) # serialize new note
        return Response(serializer.data)
    else:
        return Response("No action for this request method")

@api_view(['GET', 'PUT', 'DELETE'])
def crudNote(request, pk):
    if (request.method == 'GET'):
        note = get_object_or_404(Note, id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        data = request.data
        note = get_object_or_404(Note, id=pk)
        serializer = NoteSerializer(instance=note, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Something went wrong")
    elif (request.method == 'DELETE'):
        note = get_object_or_404(Note, id=pk)
        note.delete()
        return Response('Note was deleted')
    else:
        return Response("No action for this request method")
    
@api_view(['GET', 'POST'])
def getToDoLists(request):
    if (request.method == 'GET'):
        todolists = ToDoList.objects.all()
        serializer = ToDoListSerializer(todolists, many=True)
        return Response(serializer.data)
    elif (request.method == 'POST'): # add conditional
        data = request.data # grab data from user
        todolist = ToDoList.objects.create(title=data['title'], id=data['id']) # create new note with body property
        serializer = ToDoListSerializer(todolist, many=False) # serialize new note
        return Response(serializer.data)
    else:
        return Response("No action for this request method")
    
	# (user__username=self.request.user)

@api_view(['GET'])
def getToDoItem(request):
	if (request.method == 'GET'):
		user = request.user
		todoitems = ToDoItem.objects.all().order_by('todo_list', 'due_date')
		serializer = ToDoItemSerializer(todoitems, many=True)
		return Response(serializer.data)
	else:
		return Response("No action for this request method")