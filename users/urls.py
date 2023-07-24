from django.urls import path, include
from users.views import UserRegisterView, UserLoginView, UserLogoutView, UserChangePassword

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password_change/', UserChangePassword.as_view(), name='password_change'),
]