# Generated by Django 4.0.2 on 2022-02-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guns',
            name='description',
            field=models.TextField(max_length=1500, verbose_name='Описание товара'),
        ),
    ]
