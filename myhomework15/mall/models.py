from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

product_category = (
    ('TOP', 'Top'),
    ('PANTS', 'Pants'),
    ('OUTER', 'Outer'),
    ('SKIRT', 'Skirt'),
    ('ACC', 'Acc'),
)


class Shop(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10, choices=product_category)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField()
    photo_thumb = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(400, 200)],
        format="JPEG",
        options={"quality": 60},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
