from rest_framework import serializers
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
