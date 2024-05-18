# imports 
from django.db.models.signals import pre_save, post_save

# Custom imports
from exam.models import ExamHistory

def create_update_examhistory(sender, instance, created, **kwargs):
    print("Signal Received")

post_save.connect(create_update_examhistory, sender=ExamHistory)