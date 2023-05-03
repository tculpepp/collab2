from django.forms import ModelForm
from .models import *

# This form overrides the generic form when called and limits the ToDoLists available to the the lists 
# owned by the current user
class ToDoItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields["todo_list"].queryset = ToDoList.objects.filter(user__username=user)

    class Meta:
        model = ToDoItem
        fields = [
            "todo_list",
            "title",
            "description",
            "due_date",
        ]