from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Tenant, User, Student, Subject, Grade
from .serializers import (
    TenantSerializer, UserSerializer, StudentSerializer,
    SubjectSerializer, GradeSerializer
)
from .forms import StudentForm, CustomUserCreationForm

# =============================================
# دوال الواجهات الأمامية (UI Views)
# =============================================

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            from .models import Tenant
            tenant = Tenant.objects.first()
            if not tenant:
                tenant = Tenant.objects.create(name='المدرسة الافتراضية', subdomain='default')
            user.tenant = tenant
            user.save()
            messages.success(request, 'تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_list(request):
    from .models import Tenant
    if request.user.tenant:
        students = Student.objects.filter(tenant=request.user.tenant)
    else:
        first_tenant = Tenant.objects.first()
        if first_tenant:
            students = Student.objects.filter(tenant=first_tenant)
        else:
            students = Student.objects.none()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_create(request):
    from .models import Tenant
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            if request.user.tenant:
                student.tenant = request.user.tenant
            else:
                tenant = Tenant.objects.first()
                if not tenant:
                    tenant = Tenant.objects.create(name='المدرسة الافتراضية', subdomain='default')
                student.tenant = tenant
            student.save()
            messages.success(request, 'تم إضافة الطالب بنجاح!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    from .models import Tenant
    if request.user.tenant:
        student = get_object_or_404(Student, pk=pk, tenant=request.user.tenant)
    else:
        first_tenant = Tenant.objects.first()
        student = get_object_or_404(Student, pk=pk, tenant=first_tenant)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث بيانات الطالب!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    from .models import Tenant
    if request.user.tenant:
        student = get_object_or_404(Student, pk=pk, tenant=request.user.tenant)
    else:
        first_tenant = Tenant.objects.first()
        student = get_object_or_404(Student, pk=pk, tenant=first_tenant)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'تم حذف الطالب!')
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

# =============================================
# واجهات API (REST API ViewSets)
# =============================================

class TenantViewSet(viewsets.ModelViewSet):
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Tenant.objects.all()
        return Tenant.objects.filter(id=user.tenant.id)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(tenant=user.tenant)

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Student.objects.all()
        return Student.objects.filter(tenant=user.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Subject.objects.all()
        return Subject.objects.filter(tenant=user.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Grade.objects.all()
        return Grade.objects.filter(tenant=user.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)