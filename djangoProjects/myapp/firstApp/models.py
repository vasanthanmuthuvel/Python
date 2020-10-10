from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Items(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text