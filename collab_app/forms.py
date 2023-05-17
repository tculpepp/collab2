from django.forms import ModelForm
from django.forms import DateTimeInput, DateInput
from django.forms.widgets import NumberInput
from .models import *

# This form overrides the generic form when called and limits the ToDoLists available in the lists selector
# owned by the current user. Curently used to Create and Update ToDo List items
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
            "complete"
        ]
        # this creates the date picker calendar on the form
        widgets={
            'due_date': DateInput(attrs={'type': 'date'})
        }