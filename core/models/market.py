from django.core.validators import RegexValidator
from django.db import models

from .offers_base import Entity
from .request import BaseRequest


class MarketType(Entity):
    """Модель, характеризующая тип маркета, где можно заказать еду.
    Изанчально предусматривается: магазин, ресторан"""
    market_type_id = models.AutoField(primary_key=True)
    img = models.ImageField(default='images/market-types/default.jpg', upload_to='images/market-types')

    class Meta:
        app_label = 'core'
        db_table = 'markettype'


class Market(Entity):
    """Модель, характеризующая сущность компании, которая является магазином.
    Например: пятёрочка (как сущность, со скидками, глобальным списком товаров и прочее)"""
    market_id = models.AutoField(primary_key=True)
    market_type = models.ForeignKey(MarketType, on_delete=models.CASCADE)

    img = models.ImageField(default='images/markets/default.jpg', upload_to='images/markets')
    # rating = models.OneToOneField(Rating, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'core'
        db_table = 'market'


class MarketInstance(models.Model):
    """Модель, характеризующая конкретный экземпляр маркета.
    Например: пятёрочка по определенному адресу"""
    market_instance_id = models.AutoField(primary_key=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    address = models.OneToOneField('Address', on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'core'
        db_table = 'marketinstance'

    def __str__(self):
        return f'{self.market.name} ({self.address})'


class MarketRequest(BaseRequest):
    """Модель характеризующая заявку на становления партнером сервиса"""
    categories = models.ManyToManyField('core.Category')

    class Meta:
        app_label = 'core'
        db_table = 'marketrequest'

    def __str__(self):
        return f'Заявка на партнерство ({self.request_id})'
