from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    addr = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
