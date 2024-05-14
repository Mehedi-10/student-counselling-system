from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


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


def swagger_get_serializer(serializer_class):
    return swagger_auto_schema(
        method='get',
        responses={200: openapi.Response('List retrieved successfully', serializer_class(many=True))}
    )

def swagger_post_serializer(serializer_class):
    return swagger_auto_schema(
        method='post',
        request_body=serializer_class,
        responses={201: openapi.Response('Object created successfully', serializer_class)}
    )

def swagger_detail_get_serializer(serializer_class):
    return swagger_auto_schema(
        method='get',
        responses={200: openapi.Response('Object details retrieved successfully', serializer_class)}
    )

def swagger_detail_put_delete_serializer(serializer_class):
    return swagger_auto_schema(
        methods=['put', 'delete'],
        request_body=serializer_class,
        responses={
            200: openapi.Response('Object updated successfully', serializer_class),
            204: openapi.Response('Object deleted successfully')
        }
    )