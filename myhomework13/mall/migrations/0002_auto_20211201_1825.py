# Generated by Django 3.2.9 on 2021-12-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='addr',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='shop',
            name='tel',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]