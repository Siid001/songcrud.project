from django.contrib import admin
# Register your models here.
from .models import Artiste, Song, Lyrics

@admin.register(Artiste)
class FireFlyAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')

@admin.register(Song)
class FireFlyAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'date_released', 'likes', 'artisteId')

@admin.register(Lyrics)
class FireFlyAdmin(admin.ModelAdmin):
    list_display = ('content', 'songid')