# Generated by Django 4.0.4 on 2022-05-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='appartement',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
