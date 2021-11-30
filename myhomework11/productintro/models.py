from django.db import models
from productintro.upload_to import uuid_name_upload_to

product_category = (
    ('TOP', 'Top'),
    ('PANTS', 'Pants'),
    ('SKIRT', 'Skirt'),
    ('OUTER', 'Outer'),
    ('ACC', 'Acc'),
)

class Introduce(models.Model):
    # product_name, category, color, size, price, content, photo
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=10, choices = product_category)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
