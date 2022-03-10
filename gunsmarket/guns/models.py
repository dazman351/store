from django.db import models
from django.urls import reverse




class Guns(models.Model):
    name = models.CharField("Название", max_length=50)
    author = models.CharField("Автор", max_length=50)
    country = models.CharField("Страна", max_length=50)
    year = models.IntegerField("Год выпуска")
    calibr = models.FloatField("Калибр оружия")
    quantity = models.IntegerField("В наличии")
    price = models.IntegerField("Цена за один ствол")
    image = models.ImageField("Фотография", upload_to="guns/market_guns")
    description = models.TextField("Описание товара", max_length=1500)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Все оружия'


    def get_absolute_url(self):
        return reverse('guns:description')
