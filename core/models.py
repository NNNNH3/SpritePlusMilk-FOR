from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField('Отчество', max_length=30, null=True, blank=True)
    profile_picture = models.FileField('Фото профиля', upload_to='media/profile_pictures',
                                       null=True, blank=True)
    email = models.EmailField('Адрес эл. почты', max_length=30, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    creation_dt = models.DateTimeField(null=True, blank=True, default=now())
    date_of_birth = models.DateField('Дата рождения',default=now(), blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
