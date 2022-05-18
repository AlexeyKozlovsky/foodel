from django.db import models


class Place(models.Model):
    """Прокси модель, для вынесения данных о гео объекте"""
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    altitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(Place):
    """Модель, характеризующая страну.
    Содержит информацию о: названии, описании, изображении"""
    country_id = models.AutoField(primary_key=True)
    img = models.ImageField(default='images/country/default.jpg', upload_to='images/country')

    class Meta:
        app_label = 'core'
        db_table = 'country'


class City(Place):
    """Модель, характеризующая город.
    Содержит информацию о: названии, описании, изображении и стране."""
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    img = models.ImageField(default='images/city/default.jpg', upload_to='images/city')

    class Meta:
        app_label = 'core'
        db_table = 'city'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)

    street = models.CharField(max_length=127)
    house = models.CharField(max_length=63)
    appartement = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        app_label = 'core'
        db_table = 'address'

    def __str__(self):
        return f'{self.city.country}, {self.city}, ул. {self.street}, д. {self.house}, ' \
               f'кв. {self.appartement}'
