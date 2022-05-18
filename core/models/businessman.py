from django.db import models


class Businessman(models.Model):
    """Модель, характеризующая пользователя - работника маркета.
    Характеризуется как продавец (в общем случае)"""
    businessman_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('BaseUser', on_delete=models.CASCADE)
    market = models.ForeignKey('Market', on_delete=models.CASCADE)

    class Meta:
        app_label = 'core'
        db_table = 'businessman'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
