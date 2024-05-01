from django.db import models

# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length = 100)

class Topic(models.Model):
    field = models.ForeignKey(Field, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name