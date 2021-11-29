from django.db import models

gender_choice = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
)

class Membership(models.Model):
    # name, gender, birthday, height, join_reason
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices = gender_choice)
    birthday = models.DateField()
    height = models.IntegerField()
    join_reason = models.TextField()


