# Generated by Django 3.1.1 on 2021-05-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210527_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedimages',
            name='img',
        ),
        migrations.AddField(
            model_name='generatedimages',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
