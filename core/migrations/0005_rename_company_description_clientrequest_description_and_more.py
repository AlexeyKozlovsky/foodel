# Generated by Django 4.0.4 on 2022-05-15 18:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_bank_clientrequest_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientrequest',
            old_name='company_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='clientrequest',
            old_name='company_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='clientrequest',
            old_name='company_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='clientrequest',
            old_name='client_request_id',
            new_name='request_id',
        ),
        migrations.CreateModel(
            name='MarketRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(default='images/companies/default.jpg', upload_to='')),
                ('address', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='(?:(^[а-яА-Я]+)\\,?)\\s*(?:(?:г\\.?\\s*)([а-яА-Я]+)\\,?)\\s*(?:(?:ул)\\.?\\s*((?:[а-яА-Я]|\\s)+)\\,?)\\s*(?:(?:д)\\.?\\s*([а-яА-Я0-9]+)\\,?)\\s*(?:(?:кв|к)\\.?\\s*([а-яА-Я0-9]+))?$')])),
                ('account_num', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\d{20}$')])),
                ('TIN_num', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')])),
                ('corr_account_num', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\d{20}$')])),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.bank')),
                ('categories', models.ManyToManyField(to='core.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
