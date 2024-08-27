from datetime import datetime
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.template.context_processors import request

from final.models import CustomUser, Appointment, Email, ContactUs, ResetPassword
from django.contrib import messages
from django.contrib.messages import error
from django.contrib.auth import authenticate, login
from final.auth import MyCustomBackend


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    return render(request, 'signup.html')


def login_page(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def service(request):
    return render(request, 'service.html')


def appointment(request):
    return render(request, 'appointment.html')


"""
def save_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('Email')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        password = make_password(request.POST.get('password'))  # Hash password
        phone_number = request.POST.get('phone_number')
        # phone_number = request.POST.get('phoneNumber')

        # if not first_name:
        #     return render(request, 'signup.html', {'error_message': 'Please enter your first name'})

        # Validate form data
        # if not (first_name and last_name and email and gender and password and phone_number):
        #     return HttpResponse("All fields are required", status=400)  # Bad request

        # Save sign up form to database
        jj = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            # email=email,
            username=username,
            gender=gender,
            password=password,
            phone_number=phone_number
        )
        jj.save();
        print("User created successfully")
        return redirect('login')  # Redirect to login page after successful signup
    else:
        return render(request, "signup.html")"""


def save_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('Email')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        password = make_password(request.POST.get('password'))  # Hash password
        phone_number = request.POST.get('phone_number')
        """jj = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                # email=email,
                username=username,
                gender=gender,
                password=password,
                phone_number=phone_number
            )
            jj.save();
            return HttpResponse("User created successfully")
            return redirect('login')"""
        # Create and save the user
        try:
            # Check if the username already exists
            if not CustomUser.objects.filter(username=username).exists():
                jj = CustomUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    # email=email,
                    username=username,
                    gender=gender,
                    password=password,
                    phone_number=phone_number
                )
                jj.save();
                messages.success(request, "User created successfully")
                return redirect('login')
            else:
                # return HttpResponse("User already exists")
                messages.error(request, "User already exists")
                return redirect('signup')

        except IntegrityError as e:
            messages.error(request, "An error occurred while creating user: {}".format(e))
    else:
        return render(request, "signup.html")


"""
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('Email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
        user.save();
        return redirect('login')

    else:
        return "Please enter your first name"
"""


def make_appointment(request):
    if request.method == 'POST':
        app_ser = request.POST.get('app_ser')
        app_doc = request.POST.get('app_doc')

        ser_name = {
            'Check up': 'Check up',
            'Surgery': 'Surgery',
            'Test': 'Test',
        }.get(app_ser, 'Unknown Service')

        doc_name = {
            'Justice': 'Dr. Justice',
            'Eugene': 'Eugene',
            'Prosper': 'Prosper',
        }.get(app_doc, 'Unknown Doctor')

        app_user_name = request.POST.get('app_user_name')
        app_email = request.POST.get('app_email')
        app_date = request.POST.get('app_date')
        app_time = request.POST.get('app_time')

        try:
            app_date = datetime.strptime(app_date, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Invalid date format")

        try:
            app_time = datetime.strptime(app_time, '%H:%M').time()
        except ValueError:
            return HttpResponse("Invalid time format. Please use HH:MM")

        mm = Appointment.objects.create(
            app_ser=app_ser,
            app_doc=app_doc,
            app_user_name=app_user_name,
            app_email=app_email,
            app_date=app_date,
            app_time=app_time
        )
        mm.save()
        messages.success(request, "Appointment created successfully")
        return redirect('appointment')


def login_dashboard(request, user):
    return render(request, 'dashboard.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate using the custom backend
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'dashboard.html')
        else:
            # error(request, 'Invalid username or password.')
            return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_page')


def dashboard(request):
    return render(request, 'dashboard.html')


def subcribe_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not Email.objects.filter(email=email).exists():
            mm = Email.objects.create(email=email)
            mm.save()
            messages.success(request, "Email Subscribed", extra_tags='subscribe_email_success')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, "Email already subscribed")
            return render(request, 'contact.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        con = ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        con.save()
        print("Received message:", message)
        messages.success(request, "Message Sent Successfully", extra_tags='message_sent_successfully')
        return redirect('contact')
    else:
        messages.error(request, "Please enter your name!")
        return render(request, 'contact.html')


def password(request):
    return render(request, 'password.html')


def reset_password(request):
    if request.method == 'POST':
        password_email = request.POST.get('password_email')

        reset = ResetPassword.objects.create(email=password_email)
        reset.save()
        return redirect('login')
    else:
        return render(request, 'password.html')

