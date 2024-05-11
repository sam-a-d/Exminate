from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# imports
from root.models import Teacher, Field

# Create your models here.
class Course(models.Model):
    
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    teacher = models.ManyToManyField(Teacher)
    field = models.ManyToManyField(Field)
    is_active = models.BooleanField(default=True)
    description = models.TextField()

    total_marks = models.PositiveIntegerField(default=100)

    def __str__(self) -> str:
        return self.title
    
# Course verification token
class CourseVerificationToken(models.Model):

    token_code = models.CharField(max_length=10, null=False, default='BS123')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE),
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "coursevertoken"
        verbose_name_plural = "coursevertokens"

    def __str__(self):
        return self.token_code

# Course history - who have taken which courses and when
class CourseHistory(models.Model):

    course = models.ForeignKey(Course, models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    enrolment_time = models.DateTimeField(auto_now_add=True)
    veri_code_used = models.CharField(max_length=10)

    class Meta:
        verbose_name = "coursehistory"
        verbose_name_plural = "coursehistories"

    def __str__(self):
        return self.course_id