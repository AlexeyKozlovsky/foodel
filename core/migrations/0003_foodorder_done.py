# Generated by Django 4.0.4 on 2022-05-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_address_appartement_alter_city_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
