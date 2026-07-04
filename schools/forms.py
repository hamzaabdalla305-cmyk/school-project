from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, User

# نموذج إدارة الطلاب (إضافة، تعديل)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'student_id']
        labels = {
            'name': 'الاسم',
            'email': 'البريد الإلكتروني',
            'student_id': 'رقم الطالب',
        }

# نموذج إنشاء حساب جديد (Sign Up)
class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[('student', 'طالب'), ('teacher', 'مدرس')],
        label='الدور'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']