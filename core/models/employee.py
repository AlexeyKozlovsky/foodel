from django.db import models


class Employee(models.Model):
    """Модель, характеризующая пользователя - сотрудника компании.
    В системе выступает как заказчик"""
    emp_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('BaseUser', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    monthly_money = models.DecimalField(max_digits=10, decimal_places=2)
    addresses = models.ManyToManyField('Address')

    class Meta:
        app_label = 'core'
        db_table = 'employee'

    def __str__(self):
        return str(self.user)
