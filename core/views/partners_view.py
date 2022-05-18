from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView

from core.forms.partners import PartnerRequestForm


class PartnersView(TemplateView):
    template_name = 'core/pages/partners-page.html'
    extra_context = {'partners': []}


class PartnerRequestView(CreateView):
    template_name = 'core/pages/partner-request-page.html'
    form_class = PartnerRequestForm
    success_url = reverse_lazy('core:home')
