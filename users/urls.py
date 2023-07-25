from django.urls import path, include
from users.views import (UserRegisterView, UserLoginView, UserLogoutView,
                         UserChangePassword,
                         PasswordResetView, UserForgotPasswordView, UserEmailConfirm, EmailConfirmationSendView,
                         EmailConfirmed, EmailFiledConfirmed)

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    # path('password_change/', UserChangePassword.as_view(), name='password_change'),
    path('password_reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set_new_password/<uidb64>/<token>/', PasswordResetView.as_view(), name='set_new_password'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserEmailConfirm.as_view(), name='confirm_email'),
    path('email_confirmation_sent/', EmailConfirmationSendView.as_view(), name='email_confirmation_sent'),
    path('email_confirmed/', EmailConfirmed.as_view(), name='email_confirmed'),
    path('email_filed_confirm/', EmailFiledConfirmed.as_view(), name='email_filed_confirm'),
]