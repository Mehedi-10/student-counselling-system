# decorators.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import UserSerializer

def swagger_register_user():
    return swagger_auto_schema(
        method='post',
        request_body=UserSerializer,
        responses={201: openapi.Response('Registration Success', UserSerializer)},
        operation_description="Register a new user"
    )

def swagger_login_user():
    return swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
        ),
        responses={
            200: openapi.Response('Login Success'),
            401: openapi.Response('Unauthorized')
        },
        operation_description="Authenticate a user and retrieve a token"
    )
