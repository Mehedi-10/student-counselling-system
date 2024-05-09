from rest_framework import serializers
from .scs_models.admin_controlled_models import *
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_student', 'is_teacher']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_student=validated_data.get('is_student', False),
            is_teacher=validated_data.get('is_teacher', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'web_address', 'country', 'state', 'statement', 'status']


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', 'university', 'web_address', 'address', 'statement', 'status']


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ['id', 'name', 'web_address', 'country', 'state', 'city', 'statement', 'status']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'college', 'campus', 'web_address', 'address', 'statement', 'status']


class FacultyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMember
        fields = ['id', 'name', 'email', 'department', 'campus', 'college', 'web_address', 'address', 'statement',
                  'faculty_type', 'status']


class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ['id', 'name', 'start_date', 'end_date', 'funding_type', 'number_of_positions', 'department', 'campus',
                  'college', 'statement', 'status']
