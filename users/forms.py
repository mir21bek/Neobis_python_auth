from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
                                       SetPasswordForm, PasswordResetForm,
                                       )
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationsForm(UserCreationForm):
    email = forms.EmailField(
        label=_('email'),
        max_length=255,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def clean_emil(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder': 'Придумайте свой логин'})
            self.fields['email'].widget.attrs.update({'placeholder': 'Введите свой email'})
            self.fields['password1'].widget.attrs.update({'placeholder':  'Придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({'placeholder': 'Повторите придуманный пароль'})
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class FormChangePassword(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form control',
                'autocomplete': 'off'
            })


class ForgotPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form control',
                'autocomplete': 'off'
            })


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form control',
                'autocomplete': 'off'
            })
