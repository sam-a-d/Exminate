from django.db import models

# Imports
from root.models import Topic, Field
from course.models import Course

# Create your models here.


DIFFICULTY_CHOI = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)

class Exam(models.Model):
    name = models.CharField(max_length = 120)
    course = models.ManyToManyField(Course)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    exam_description = models.TextField(max_length = 120)
    no_of_questions = models.IntegerField()
    total_marks = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)
    difficulty_level = DIFFICULTY_CHOI

    def get_mcqs(self):
        pass

    def __str__(self) -> str:
        return f'{self.name} - Topic: {self.topic}'