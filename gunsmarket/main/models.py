from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=100)
    phone = models.CharField("Номер телефона", max_length=30)
    email2 = models.EmailField("Ваш второй email", max_length=50, null=True, blank=True)
    image = models.ImageField("Фотография", upload_to='main/profile_img', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)


    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk': self.user.id})


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # id=instance.id

@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()