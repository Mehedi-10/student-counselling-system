from django.http import JsonResponse
from functools import wraps
from ..models import User
from datetime import datetime, timedelta

def token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'error': 'Token is missing'}, status=401)

        try:
            # Assuming the token is in the format "Token <actual_token_here>"
            token = token.split()[1]
            user = User.objects.get(token=token)
            if datetime.now() - user.token_created_at > timedelta(hours=1):  # 1 hour token validity
                return JsonResponse({'error': 'Token has expired'}, status=401)
            request.user = user  # Attach user to request
        except (User.DoesNotExist, IndexError, ValueError):
            return JsonResponse({'error': 'Invalid token'}, status=401)

        return f(request, *args, **kwargs)

    return decorated
