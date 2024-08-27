from django.urls import path
from . import views
from .views import login_view
from .views import save_signup

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/register', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout, name='logout'),
    path('service/', views.service, name='service'),
    path('appointment/', views.appointment, name='appointment'),
    path('signup/save_signup', views.save_signup, name='save_signup'),
    path('login/login_view', views.login_view, name='login_view'),
    path('login_dashboard', views.login_dashboard, name='login_dashboard'),
    path('appointment/make_appointment', views.make_appointment, name='make_appointment'),
    path('appointment/subcribe_email', views.subcribe_email, name='subcribe_email'),
    path('contact/subcribe_email', views.subcribe_email, name='subcribe_email'),
    path('subcribe_email', views.subcribe_email, name='subcribe_email'),
    path('service/subcribe_email', views.subcribe_email, name='subcribe_email'),
    path('about/subcribe_email', views.subcribe_email, name='subcribe_email'),
    path('contact/contactus', views.contactus, name='contactus'),
    path('login/password', views.password, name='password'),
    path('login/reset_password', views.reset_password, name='reset_password')
]