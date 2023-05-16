from django.forms import ModelForm
from django.forms import DateTimeInput
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
        # this defines the format for the DateTimeInput
        # in this case:'10/25/06 14:30'
        # other formats: https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DATETIME_INPUT_FORMATS
        widgets={
            'due_date':DateTimeInput(format='%m/%d/%y')
        }