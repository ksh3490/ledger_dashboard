from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('sign_up', views.sign_up, name="sign up"),
]