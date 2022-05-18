from django.views.generic import TemplateView

from core.models import Company


class MainView(TemplateView):
    template_name = 'core/pages/main-page.html'
    extra_context = {'main_companies': Company.objects.all()[:2]}
