from django.db import models

# imports
from exam.models import Exam

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    # teacher = 
    # area = 
    exams = models.ManyToManyField(Exam)
    description = models.TextField()


    def __str__(self) -> str:
        return self.title