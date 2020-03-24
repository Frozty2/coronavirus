"""Importing models, which are data informations from django.db"""
from django.db import models


class Todo(models.Model):
    """Crate field in data base for 'to do' sentences and publication date"""
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
