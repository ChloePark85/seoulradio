# Generated by Django 2.1.2 on 2018-10-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='place',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=20),
        ),
    ]
