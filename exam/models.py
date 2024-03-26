from django.db import models

# Create your models here.

class Field(models.model):
    name = models.CharField(max_length = 100)

class Topic(models.Model):
    field = models.ForeignKey(Field, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

DIFFICULTY_CHOI = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)

class Exam(models.Model):
    name = models.CharField(max_length = 120)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    exam_description = models.CharField(max_length = 120)
    no_of_questions = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)
    difficulty_level = DIFFICULTY_CHOI

    def get_mcqs(self):
        pass

    def __str__(self) -> str:
        return f'{self.name} - Topic: {self.topic}'