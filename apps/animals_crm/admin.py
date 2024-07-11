from django.contrib import admin
from .models import AnimalPhoto, AnimalCard, AnimalComment

admin.site.register(AnimalCard)
admin.site.register(AnimalPhoto)
admin.site.register(AnimalComment)
