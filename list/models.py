from django.db import models

# Create your models here.
class Todo (models.Model):
    todo = models.TextField()
    created_date = models.DateTimeField(auto_now_add =True)
    due_date = models.DateTimeField()
    done = models.BooleanField(default = False)

    def __str__(self):
        return self.todo
