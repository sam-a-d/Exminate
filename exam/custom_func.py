
""" This file contains custom defind functions
"""

# imports
from question.models import MCQ, ShortQues, LongQues
from exam.models import McqAndShortQExamHistory, LongQExamHistory

def process_mcq_and_shortQ(user_id, exam_id, ques_type,  answer_dict):
    
    # retrive all the questions related to the exam
    if ques_type == 1:
        all_mcqs_of_the_exam = MCQ.objects.filter(exam=exam_id)
    elif ques_type == 2:
        all_shortQ_of_the_exam = ShortQues.objects.filter(exam=exam_id)

    # mcq_id = 0

    total_score = 0

    for question, ans in answer_dict.items():
        if ques_type == 1:
            mcq_id = int(question[len('mcq_'):]) # mcq exam retrived from the form that students filled during their exam
            mcq_details = all_mcqs_of_the_exam.get(pk=mcq_id) # get the mcq details from the MCQ models (database)
            score = mcq_details.mark if mcq_details.right_ans.lower() == ans.lower() else 0

        elif ques_type == 2:
            shortQ_id = int(question[len('sq_'):]) # short ques exam retrived from the form that students filled during their exam
            shortQ_details = all_shortQ_of_the_exam.get(pk=shortQ_id) # get the mcq details from the MCQ models (database)
            score = shortQ_details.mark if shortQ_details.answer == ans else 0
        
        McqAndShortQExamHistory.objects.create(
            user_id=user_id,
            exam_id=exam_id,
            question_type= ques_type,
            question_id=mcq_id if ques_type == 1 else shortQ_id,
            user_answer=ans,
            score=score
        )

        total_score += score

        # return (mcq_id, ans, score)
    return total_score

def process_longQ(user_id, exam_id, ques_type,  answer_dict):
    total_score = 0
    
    all_lq_of_the_exam = LongQues.objects.filter(exam=exam_id)

    for question, ans in answer_dict.items():

        lq_id = int(question[len('lq_'):]) # mcq exam retrived from the form that students filled during their exam
        question_details = all_lq_of_the_exam.get(pk=lq_id) # get the mcq details from the MCQ models (database)

        LongQExamHistory.objects.create(
            user_id=user_id,
            exam_id=exam_id,
            question_id=lq_id,
            user_answer=ans,
        )
    
    return None