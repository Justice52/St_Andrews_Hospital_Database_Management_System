from django.contrib.auth.backends import ModelBackend
from .models import CustomUser  # Replace with your custom user model name


class MyCustomBackend(ModelBackend):
    '''Custom authentication backend for your user model.'''

    def authenticate(self, request, username=None, password=None):
        if username is None:
            username = request.POST.get('username')
        if password is None:
            password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            pass
        return None
