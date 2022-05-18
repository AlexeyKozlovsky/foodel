from django.db import models

from .offers_base import Entity


class Category(Entity):
    """Модель, характеризующая категорию товаров.
    Модель должна содержат данные о названии, описании и изображении категории"""
    category_id = models.AutoField(primary_key=True)
    category_parent = models.ForeignKey(null=True, blank=True, to='Category', on_delete=models.PROTECT)

    img = models.ImageField(default='images/categories/default.jpg', upload_to='images/categories')

    class Meta:
        app_label = 'core'
        db_table = 'category'


class Good(Entity):
    """Модель, характеризующая товар.
    Модель содержит информацию о маркете, к которому привязан товар,
    название, описание и изображение товара"""
    good_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    market = models.ForeignKey('Market', on_delete=models.CASCADE)

    proteins = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fats = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    carbohydrates = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    calories = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    img = models.ImageField(default='images/goods/default.jpg', upload_to='images/goods')
    # rating = models.OneToOneField(Rating, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'core'
        db_table = 'good'


class GoodInstance(models.Model):
    """Модель, характеризующая информацию о конкретных экземплярах товара.
    Модель содержит информацию о конкретном маркете, где этот конкретный товар имеется
    и в каком количество. А так же, модель содержит информацию о том, что это за товар (см. модель Good)"""
    good_instance_id = models.AutoField(primary_key=True)
    good = models.ForeignKey('Good', on_delete=models.CASCADE)
    market_instance = models.ForeignKey('MarketInstance', on_delete=models.CASCADE)
    good_servings = models.ManyToManyField(to='GoodServing')

    count = models.IntegerField()

    class Meta:
        app_label = 'core'
        db_table = 'goodinstance'

    def __str__(self):
        return f'{self.good.name}; {self.market_instance}'


class GoodServing(models.Model):
    good_serving_id = models.AutoField(primary_key=True)
    weight = models.IntegerField()     # В граммах
    caption = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        app_label = 'core'
        db_table = 'goodserving'

    def __str__(self):
        return self.caption

