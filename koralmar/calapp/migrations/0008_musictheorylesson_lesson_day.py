# Generated by Django 4.2.9 on 2024-02-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0007_alter_musictheorylesson_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='musictheorylesson',
            name='lesson_day',
            field=models.DateField(default='2024-02-23'),
            preserve_default=False,
        ),
    ]
