from django.db import models

# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    field = models.ForeignKey(Field, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # Affiliation = 
    # Designation = 
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
