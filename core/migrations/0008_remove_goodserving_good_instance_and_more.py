# Generated by Django 4.0.4 on 2022-05-16 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_category_category_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodserving',
            name='good_instance',
        ),
        migrations.AddField(
            model_name='goodinstance',
            name='good_servings',
            field=models.ManyToManyField(to='core.goodserving'),
        ),
        migrations.AlterField(
            model_name='goodinstance',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.good'),
        ),
    ]
