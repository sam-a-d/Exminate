from django.db import models

from exam.models import Exam
from root.models import Field, Topic

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        """Unicode representation of Designation."""
        return self.name

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
    mark = models.PositiveIntegerField(default=2, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Designation."""
        return self.question

class ShortQues(models.Model):

    # Meta
    field = models.ManyToManyField(Field)
    tag = models.ManyToManyField(Tag)
    exam = models.ManyToManyField(Exam)

    question = models.TextField(max_length=1200)
    answer = models.CharField(max_length=100)
    mark = models.PositiveIntegerField(default=5, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Designation."""
        return self.question

class LongQues(models.Model):

    # Meta
    field = models.ManyToManyField(Field)
    tag = models.ManyToManyField(Tag)
    exam = models.ManyToManyField(Exam)
    
    question = models.TextField(max_length=1200)
    mark = models.PositiveIntegerField(default=10, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Designation."""
        return self.question