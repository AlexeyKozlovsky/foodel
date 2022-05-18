from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.core.exceptions import ValidationError

from core.models import BaseUser


class BaseUserCreationForm(forms.ModelForm):
    """Форма для создания пользователя.
    Будет использоваться по началу только в админке"""
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = BaseUser
        fields = ('email', 'phone', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class BaseUserChangeForm(forms.ModelForm):
    """Форма для редактирования данных о пользователе через админскую панель"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = BaseUser
        fields = ('email', 'phone', 'first_name', 'last_name', 'password', 'is_active', 'is_superuser')


class LoginForm(AuthenticationForm, forms.ModelForm):
    """Форма для авторизации пользователя. Будет использоваться на сайте для входа"""
    username = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-input',
                                                                             'placeholder': 'Email',
                                                                             'autocomplete': 'new-email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'placeholder': 'Пароль',
                                                                                 'autocomplete': 'new-password'}))

    class Meta:
        model = BaseUser
        fields = ('username', 'password')
