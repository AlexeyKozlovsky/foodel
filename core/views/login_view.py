from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from core.forms.auth_user_forms import LoginForm


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'core/pages/login-page.html'
    success_url = reverse_lazy('core:profile')
    next_page = reverse_lazy('core:profile')


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('core:login')
