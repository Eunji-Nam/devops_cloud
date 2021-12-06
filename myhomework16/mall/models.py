from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
