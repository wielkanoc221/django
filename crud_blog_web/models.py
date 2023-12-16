from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Kolejny(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=False)

    def __str__(self):
        return self.title


class Trzeci(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
