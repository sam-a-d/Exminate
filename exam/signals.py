# imports 
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Custom imports
from exam.models import ExamHistory, LongQExamHistory

@receiver(post_save, sender=LongQExamHistory) # receiver decorator same as post_save.connect(create_update_examhistory, sender=LongQExamHistory)
def create_update_examhistory(sender, instance, created, **kwargs):
    
    longQ_score = instance.score
    evaluated = instance.evaluated
    
    if not created: #update examhistory table if existing record is found thus new record is not created
    
        ExamHistory.objects.update_or_create(
        
            exam=instance.exam_id,
            user= instance.user_id,
            
            defaults = {
                'longQ_score' : instance.score,
                'evaluated' : True if instance.evaluated else False
            }
        )

