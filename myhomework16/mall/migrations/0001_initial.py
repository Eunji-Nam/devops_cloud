# Generated by Django 3.2.9 on 2021-12-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]