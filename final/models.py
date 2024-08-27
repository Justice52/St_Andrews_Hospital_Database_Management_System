from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# from django.contrib.auth.hashers import make_password

"""
# Create your models here.
class SignUp(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password, gender, phone_number):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, username=username, password=password,
                          gender=gender, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)

    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'gender', 'phone_number', 'email']

    objects = SignUp()

    def __str__(self):
        return self.email"""

"""
class MyCustomBackend(ModelBackend):
    
    Custom authentication backend for your user model.
    

    def authenticate(self, request, username, password):
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
        return None"""


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, password, gender, phone_number, **extra_fields):
        # if not email:
        #     raise ValueError('The Email field must be set')
        # email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, username=username, gender=gender,
                          phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, password, gender, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(first_name, last_name, username, password, gender, phone_number, **extra_fields)

    def make_app(self, app_ser, app_doc, app_user_name, app_email, app_date, app_time):
        app = self.model(app_ser=app_ser, app_doc=app_doc, app_user_name=app_user_name, app_email=app_email,
                         app_date=app_date, app_time=app_time)
        app.save(using=self._db)
        return app


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'phone_number', 'password']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Appointment(models.Model):
    # SERVICE_CHOICES = (
    #     (1, 'Check Up'),
    #     (2, 'Surgery'),
    #     (3, 'Test'),
    # )
    #
    # DOCTOR_CHOICES = (  # Assuming you have doctor data elsewhere
    #     (1, 'Justice'),
    #     (2, 'Eugene'),
    #     (3, 'Prosper'),
    # )

    app_ser = models.CharField(max_length=100)
    app_doc = models.CharField(max_length=100)  # Store doctor's name directly
    app_user_name = models.CharField(max_length=255)
    app_email = models.EmailField()
    app_date = models.DateField()
    app_time = models.TimeField()

    def __str__(self):
        return f"{self.app_user_name} - Appointment for {self.get_service_display()} on {self.app_date} at {self.app_time.strftime('%H:%M')}"

    def get_service_display(self):
        pass


class Email(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class ResetPassword(models.Model):
    email = models.EmailField(unique=False)

    def __str__(self):
        return self.email
