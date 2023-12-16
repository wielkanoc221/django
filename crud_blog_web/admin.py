from django.contrib import admin
from django.db import models
from .models import Kolejny, Article, Trzeci

admin.site.register(Kolejny)
admin.site.register(Trzeci)
admin.site.register(Article)
# Register your models here.
