from django.db import models

# imports
from root.models import Teacher, Field

# Create your models here.
class Course(models.Model):
    
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    teacher = models.ManyToManyField(Teacher)
    field = models.ManyToManyField(Field)
    description = models.TextField()

    total_marks = models.PositiveIntegerField(default=100)

    def __str__(self) -> str:
        return self.title