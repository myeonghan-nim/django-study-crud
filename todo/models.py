from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=20)
    due_date = models.DateField()
