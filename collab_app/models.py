# collaborator/todo_app/models.py
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# May remove this, have stopped using it for now
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# create the DB model for the todo lists
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, default=" ", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

#  create the DB model for the todo list items
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]