from django.db import models

from exam.models import Exam
from root.models import Field, Topic

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=15)

# Model for MCQ questions
class MCQ(models.Model):
    
    # Meta informations
    field = models.ManyToManyField(Field, blank=True)
    Topic = models.ManyToManyField(Topic, blank=True)
    exam = models.ManyToManyField(Exam)
    tag = models.ManyToManyField(Tag)

    # Question and answer
    question = models.TextField(max_length=1200)
    a = models.CharField(max_length=400)
    b = models.CharField(max_length=400)
    c = models.CharField(max_length=400)
    d = models.CharField(max_length=400)

    # MCQ options
    options = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )
    # Answer and the marks
    right_ans = models.CharField(max_length=100, choices=options)
    mark = models.PositiveIntegerField(default=1, null=True, blank=True)
