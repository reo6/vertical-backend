from django.contrib import admin
from .models import Author, Category, Podcast

admin.site.register(Podcast)
admin.site.register(Author)
admin.site.register(Category)
