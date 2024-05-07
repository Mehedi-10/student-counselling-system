import json

from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import secrets
from datetime import datetime
from .middlewares.auth_middlewares import token_required
from .models import User, Student, Teacher


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        user_type = data.get('user_type')

        # Basic validation
        if not email or not password:
            return JsonResponse({'error': 'Email and password required'}, status=400)
        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already in use'}, status=400)

        try:
            with transaction.atomic():
                # Create the user
                user = User(email=email, password=make_password(password))
                user.is_teacher = user_type == 'teacher'
                user.is_student = user_type == 'student'
                user.save()

                if user_type == 'student':
                    Student.objects.create(user=user)
                elif user_type == 'teacher':
                    Teacher.objects.create(user=user)

                return JsonResponse({'message': 'User registered successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': 'Failed to register user. ' + str(e)}, status=500)


def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email and password required'}, status=400)

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                token = secrets.token_urlsafe()
                user.token = token
                user.token_created_at = datetime.now()
                user.save()

                user_type = 'teacher' if user.is_teacher else 'student'
                return JsonResponse({
                    'message': 'Login successful',
                    'token': token,
                    'expires_in': 3600,  # Token expiry in seconds (e.g., 1 hour)
                    'user_type': user_type
                }, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)


@token_required
def home(request):
    user = request.user  # Directly use the user object attached to the request
    if user.is_teacher:
        welcome_message = f"Welcome, Teacher {user.email}!"
    elif user.is_student:
        welcome_message = f"Welcome, Student {user.email}!"
    else:
        welcome_message = "Welcome!"

    return JsonResponse({'message': welcome_message}, status=200)
