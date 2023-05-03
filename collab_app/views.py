# collaborator/collab_app/views.py
# This file defines the views and functions for the app
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ToDoItemForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import ToDoItem, ToDoList

# LoginRequiredMixin is used on all pages that require a user to be logged in to access
# All view classes utilize Django built-in generic class view as a base


# define the list view that is used in the index.html template
class ListListView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = "collab_app/index.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    # create two return datasets. one for the current user and one for all other users
    def get_context_data(self):
        context_data = super().get_context_data()
        context_data['currentUserData'] = ToDoList.objects.filter(user__username=self.request.user)
        context_data['otherUserData'] = ToDoList.objects.exclude(user__username=self.request.user)
        return context_data

# This class defines how the list items look when loaded with todo_list.html
class ItemListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    template_name = "collab_app/todo_list.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    # filter the DB for the current list's items only
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    #  turn the query into a context object (dictionary)
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

# This class is for creating new list shells
class ListCreate(LoginRequiredMixin, CreateView):
    model = ToDoList
    login_url = '/accounts/login/' # mark for possible removal. depreciated
    redirect_field_name = 'redirect_to'
    fields = [
        "title"
        ]

    def form_valid(self, form):
         user = self.request.user
         form.instance.user = user
         return super(ListCreate, self).form_valid(form)
    
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

#  this class creates new items for a todo list
class ItemCreate(LoginRequiredMixin, CreateView):
    model = ToDoItem
    login_url = '/accounts/login/' # mark for possible removal. depreciated
    redirect_field_name = 'redirect_to'
    form_class = ToDoItemForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user 
        return kwargs
    
    # def get_initial(self):
    #     initial_data = super(ItemCreate, self).get_initial()
    #     print('initial data (create):') # delete me
    #     print(initial_data) # delete me
    #     return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        print("todo_list (Create):") # delete me
        print(context['todo_list']) # delete me
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

# this class allows a user to update an item on a todo list
class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = ToDoItem
    login_url = '/accounts/login/' # mark for possible removal. depreciated
    redirect_field_name = 'redirect_to'
    form_class = ToDoItemForm
    # fields = [
    #     "todo_list",
    #     "title",
    #     "description",
    #     "due_date",
    # ]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user 
        return kwargs

    # def get_initial(self):
    #     initial_data = super(ItemUpdate, self).get_initial()
    #     print('initial data (update):') # delete me
    #     print(initial_data) # delete me
    #     return initial_data
    
    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        print("todo_list (Update):") # delete me
        print(context['todo_list']) # delete me
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

# class to allow deletion of complete lists 
class ListDelete(LoginRequiredMixin, DeleteView):
    model = ToDoList
    login_url = '/accounts/login/' # mark for possible removal. depreciated
    redirect_field_name = 'redirect_to'
    # reverse_lazy() is used here because the URLs do not load when the file does
    success_url = reverse_lazy("index")

# class for the deletion of individual list items
class ItemDelete(LoginRequiredMixin, DeleteView):
    model = ToDoItem
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
