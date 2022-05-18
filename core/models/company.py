from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from core.models import BaseRequest


class Company(models.Model):
    """Модель, характеризующая компанию.
    Модель должна хранить информацию о названии, описании,
    адресе, изображении компании, а также информацию о том, сколько
    денег должна тратить компания на сотрудника по общим условиям"""
    company_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Количество денег, которые компания может потратить на сотрудника в месяц
    # (без учета персональных условий)
    monthly_money = models.DecimalField(max_digits=10, decimal_places=2)

    img = models.ImageField(default='images/companies/default.jpg', upload_to='images/companies')

    class Meta:
        app_label = 'core'
        db_table = "company"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_slug': self.slug})


class ClientRequest(BaseRequest):
    """Модель, характеризующая запрос на становление клиентом сервиса"""
    employees_count = models.PositiveIntegerField()
    employee_money = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        app_label = 'core'
        db_table = 'clientrequest'

    def __str__(self):
        return f'Заявка на становление клиентом ({self.request_id})'
