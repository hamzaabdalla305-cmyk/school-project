from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TenantViewSet, UserViewSet, StudentViewSet, 
    SubjectViewSet, GradeViewSet
)

router = DefaultRouter()
router.register(r'tenants', TenantViewSet, basename='tenant')
router.register(r'users', UserViewSet, basename='user')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'grades', GradeViewSet, basename='grade')

urlpatterns = [
    path('', include(router.urls)),
]