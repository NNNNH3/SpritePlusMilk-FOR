# Generated by Django 4.2.7 on 2023-11-24 10:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='media/profile_pictures', verbose_name='Фото профиля')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='Адрес эл. почты')),
                ('phone_number', models.CharField(blank=True, max_length=11)),
                ('creation_dt', models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 24, 10, 22, 42, 772692, tzinfo=datetime.timezone.utc), null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, verbose_name='Дата рождения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
