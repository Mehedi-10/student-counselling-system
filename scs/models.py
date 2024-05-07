from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    token = models.CharField(max_length=256, null=True, blank=True)
    token_created_at = models.DateTimeField(null=True, blank=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    grade = models.CharField(max_length=10,null=True)
    major = models.CharField(max_length=100,null=True)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.CharField(max_length=100,null=True)
    office = models.CharField(max_length=100,null=True)


