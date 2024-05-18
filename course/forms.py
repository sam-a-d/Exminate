from django import forms

class CourseEnrolmentForm(forms.Form):
    course_code = forms.CharField(max_length=10)
    verification_token = forms.CharField(max_length=20)