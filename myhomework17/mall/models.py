from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Cloth(TimestampedModel):
    name = models.CharField(max_length=20, db_index=True)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    content = models.TextField()
    photo = models.ImageField()
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = "상품목록"

class Review(TimestampedModel):
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰목록"

class Tag(TimestampedModel):
    category = models.CharField(max_length=10, db_index=True)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그목록"
