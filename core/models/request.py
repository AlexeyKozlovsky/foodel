from django.core.validators import RegexValidator
from django.db import models


class BaseRequest(models.Model):
    """Базовая абстрактная модель для заявок.
    Будет использована как родительская для заявки клиента и заявки партнера"""
    request_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)

    name = models.CharField(max_length=255)
    description = models.TextField()

    img = models.ImageField(default='images/requests/default.jpg', upload_to='images/requests/')

    # (?:(^[а-яА-Я]+)\,?)\s*(?:(?:г\.?\s*)([а-яА-Я]+)\,?)\s*(?:(?:ул)\.?\s*((?:[а-яА-Я]|\s)+)\,?)\s*(?:(?:д)\.?\s*([а-яА-Я0-9]+)\,?)\s*(?:(?:кв|к)\.?\s*([а-яА-Я0-9]+))?$
    address_regex = RegexValidator(
        regex=r'(?:(^[а-яА-Я]+)\,?)\s*(?:(?:г\.?\s*)([а-яА-Я]+)\,?)\s*(?:(?:ул)\.?\s*((?:[а-яА-Я]|\s)+)\,?)'
              r'\s*(?:(?:д)\.?\s*([а-яА-Я0-9]+)\,?)\s*(?:(?:кв|к)\.?\s*([а-яА-Я0-9]+))?$')
    address = models.CharField(max_length=255, validators=[address_regex])

    account_num_validator = RegexValidator(regex=r'^\d{20}$')
    account_num = models.CharField(max_length=20, validators=[account_num_validator])

    bank = models.ForeignKey('core.Bank', on_delete=models.PROTECT)

    TIN_num_validator = RegexValidator(regex=r'^\d{10}$')
    TIN_num = models.CharField(max_length=10, validators=[TIN_num_validator])

    corr_account_num_validator = RegexValidator(regex=r'^\d{20}$')
    corr_account_num = models.CharField(max_length=20, validators=[corr_account_num_validator])

    class Meta:
        abstract = True
