from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *
from collab_app.models import ToDoList, ToDoItem

    
@api_view(['GET', 'POST'])
def getToDoLists(request):
    if (request.method == 'GET'):
        todolists = get_list_or_404(ToDoList.objects.filter(user__username=request.user))
        serializer = ToDoListSerializer(todolists, many=True)
        return Response(serializer.data)
    elif (request.method == 'POST'):
        data = request.data 
        print(data)
        user = request.user
        todolist=ToDoList(title=data["title"], user=user)
        todolist.save()
        serializer = ToDoListSerializer(todolist, many=False)
        return Response(serializer.data)
    else:
        return Response("No action for this request method")

@api_view(['GET', 'POST'])
def getToDoItem(request):
	if (request.method == 'GET'):
		todoitems = get_list_or_404(ToDoItem.objects.all().order_by('todo_list', 'due_date'))
		serializer = ToDoItemSerializer(todoitems, many=True)
		return Response(serializer.data)
	elif (request.method == 'POST'):
		data = request.data 
		todoitem=ToDoItem(
			title=data["title"],
			description=data['description'],
			created_date=data['created_date'],
			due_date=data['due_date'],
			todo_list=ToDoList.objects.get(id=data['todo_list']),
			)
		todoitem.save()
		serializer = ToDoListSerializer(todoitem, many=False)
		return Response(serializer.data)
	else:
		return Response("No action for this request method")