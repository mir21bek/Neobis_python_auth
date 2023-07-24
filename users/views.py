from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView, PasswordResetConfirmView,
                                       PasswordResetView)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import (UserCreationsForm, LoginForm, FormChangePassword,
                         ForgotPasswordForm, UserSetPasswordForm)


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserCreationsForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    next_page = 'home'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):
    next_page = 'home'


class UserChangePassword(PasswordChangeView):
    form_class = FormChangePassword
    template_name = 'registration/change_password.html'
    success_message = 'Ваш пароль был успешно изменён!'
    next_page = 'home'

    def get_context_data(self, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'Изменение пароля на сайте'
        return context


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    form_class = ForgotPasswordForm
    template_name = 'registration/user_reset_password.html'
    success_url = reverse_lazy('home')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'email/password_subject_reset_mail.txt'
    email_template_name = 'email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class PasswordResetView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = 'registration/user_set_password_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context
