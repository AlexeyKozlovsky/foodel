from django.core.validators import RegexValidator
from django.db import models


class Bank(models.Model):
    """Модель, характеризующая банк, с которым сотрудничает сервис"""
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=64)
    bank_description = models.TextField()

    bank_icon = models.ImageField(default='images/banks/default.png', upload_to='images/banks/')

    class Meta:
        app_label = 'core'
        db_table = 'bank'

    def __str__(self):
        return self.bank_name


class Account(models.Model):
    """Модель, характеризующая банковский счет, для проведения операций сервиса"""
    account_id = models.AutoField(primary_key=True)

    account_num_validator = RegexValidator(regex=r'^\d{20}$')
    account_num = models.CharField(max_length=20, validators=[account_num_validator])

    bank = models.ForeignKey('core.Bank', on_delete=models.PROTECT)

    TIN_num_validator = RegexValidator(regex=r'^\d{10}$')
    TIN_num = models.CharField(max_length=10, validators=[TIN_num_validator])

    corr_account_num_validator = RegexValidator(regex=r'^\d{20}$')
    corr_account_num = models.CharField(max_length=20, validators=[corr_account_num_validator])

    class Meta:
        app_label = 'core'
        db_table = 'account'

    def __str__(self):
        return f'Счет: {self.account_id}'
