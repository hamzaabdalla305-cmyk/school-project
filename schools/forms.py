from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'student_id']
        labels = {
            'name': 'الاسم',
            'email': 'البريد الإلكتروني',
            'student_id': 'رقم الطالب',
        }