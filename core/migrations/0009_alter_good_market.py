# Generated by Django 4.0.4 on 2022-05-16 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_goodserving_good_instance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.market'),
        ),
    ]
