from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# custom imports 
from .models import Exam
from question.models import MCQ, ShortQues, LongQues

# Create your views here.
class ExamListView(ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = "exam/exams.html"

class ExamDetailView(DetailView):
    model = Exam
    context_object_name = 'exam'
    template_name = "exam/exam-detail.html"

class ExamQuestionDetailView(DetailView):
    model = Exam
    context_object_name = 'exam'
    template_name = "exam/exam-questions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mcqs'] = MCQ.objects.filter(exam=self.kwargs.get('pk'))
        context['shortQues'] = ShortQues.objects.filter(exam=self.kwargs.get('pk'))
        context['longQues'] = LongQues.objects.filter(exam=self.kwargs.get('pk'))
        return context

def ExamCompleteView(request):
    """View for ExamComplete Page"""

    if request.method == "POST":
        pass   
    # print("Post Request", request.POST)
    # form = OrderForm(request.POST)

    # if form.is_valid():
    #     form.save()
    #     return redirect('orders')
    return render(request, 'exam/exam-complete.html')