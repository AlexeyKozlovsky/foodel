from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.services.users import get_concrete_user, get_addresses, get_profile_context


class UserView(TemplateView):
    template_name = 'core/pages/profile.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        context = get_profile_context(request.user)

        if context['user_type'] == 'Admin':
            return redirect('/admin')

        return render(request, self.template_name, context)
