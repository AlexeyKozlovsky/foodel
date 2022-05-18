from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView, CreateView

from core.forms.clients import ClientRequestForm


class ClientsView(TemplateView):
    template_name = 'core/pages/clients-page.html'
    extra_context = {'companies': []}


class ClientRequestView(CreateView):
    template_name = 'core/pages/client-request-page.html'
    form_class = ClientRequestForm
    success_url = reverse_lazy('home')


