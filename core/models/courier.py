from django.db import models


class Courier(models.Model):
    """Модель, характеризующая пользователя - курьера"""
    courier_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('BaseUser', on_delete=models.CASCADE)
    chief = models.ForeignKey('Businessman', on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'core'
        db_table = 'courier'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
