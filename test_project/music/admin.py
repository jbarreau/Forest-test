from django.contrib import admin

from music.models import Album, Song, Band

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Band)
