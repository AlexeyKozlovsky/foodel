from django.db import models


class FoodOrder(models.Model):
    order_id = models.IntegerField(primary_key=True, auto_created=True)
    emp = models.ForeignKey('Employee', on_delete=models.CASCADE)
    courier = models.ForeignKey('Courier', on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    tips = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    address = models.ForeignKey('Address', on_delete=models.DO_NOTHING)
    done = models.BooleanField(default=False)

    class Meta:
        app_label = 'core'
        db_table = 'foodorder'


class OrderData(models.Model):
    """Модель, характеризующая таблицу для связи данных заказа.
    Связывается сама сущность заказа, с товарами, которые необходимо привезти"""
    food_order = models.ForeignKey(to=FoodOrder, on_delete=models.CASCADE)
    good_instance = models.ForeignKey(to='GoodInstance', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        app_label = 'core'
        db_table = 'order_data'
