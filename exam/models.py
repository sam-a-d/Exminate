from django.db import models
from django.utils import timezone

# Imports
from root.models import Topic, Field
from course.models import Course

# Create your models here.


DIFFICULTY_CHOICE = (
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
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICE, default=DIFFICULTY_CHOICE[1][1])
    start_time = models.DateTimeField(auto_now=False, default=timezone.now)
    finish_time = models.DateTimeField(auto_now=False, default=timezone.now)

    def get_mcqs(self):
        pass

    def __str__(self) -> str:
        return f'{self.name} - Topic: {self.topic}'

class McqAndShortExam(models.Model):
    """ 
    this model stores information/history about each finished exam of
        - MCQ and
        - Short Question
    """
    user_id = models.IntegerField()
    exam_id = models.IntegerField()
    question_type = models.IntegerField()
    question_id = models.IntegerField()
    user_answer = models.CharField(max_length=200, default=None)
    score = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                'user_id',
                'exam_id',
                'question_type',
                'question_id',
                name="single_attempt_mcq_short_unique"
            ),
        ]
        verbose_name = "mcqandshortexam"
        verbose_name_plural = "mcqandshortexams"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mcqandshortexam_detail", kwargs={"pk": self.pk})
