from rest_framework import serializers
from .models import Tenant, User, Student, Subject, Grade

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'tenant', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # عشان كلمة السر تظهرش في الردود

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # تشفير كلمة السر تلقائياً
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'