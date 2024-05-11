from django.db import models
from django.utils import timezone

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
