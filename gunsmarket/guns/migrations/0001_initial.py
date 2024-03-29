# Generated by Django 4.0.2 on 2022-02-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('calibr', models.FloatField(verbose_name='Калибр оружия')),
                ('quantity', models.IntegerField(verbose_name='В наличии')),
                ('price', models.IntegerField(verbose_name='Цена за один ствол')),
                ('image', models.ImageField(upload_to='guns/market_guns', verbose_name='Фотография')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание товара')),
            ],
            options={
                'verbose_name': 'Оружие',
                'verbose_name_plural': 'Все оружия',
            },
        ),
    ]
