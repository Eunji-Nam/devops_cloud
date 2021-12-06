from django.db import models

procuct_category = (
    ('TOP', 'Top'),
    ('PANTS', 'Pants'),
    ('SKIRT', 'Skirt'),
    ('OUTER', 'Outer'),
    ('ACC', 'Acc'),
)


class Shop(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10, choices=procuct_category)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
