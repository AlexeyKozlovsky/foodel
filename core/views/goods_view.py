from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import GoodInstance, Category


class GoodsView(TemplateView):
    template_name = 'core/pages/food.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        goods = GoodInstance.objects.all()
        paginator = Paginator(goods, 2)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'goods': page_obj,
            'categories': Category.objects.all(),
            'selected_category': 2
        }

        return render(request, self.template_name, context)
