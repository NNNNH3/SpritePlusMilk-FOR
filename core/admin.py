from django.contrib import admin
from core import models


@admin.register(models.Profile)
class Profile(admin.ModelAdmin):
    list_display = ('id',)
