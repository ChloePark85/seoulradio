# Generated by Django 2.1.2 on 2018-10-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('place', models.TextField()),
                ('title', models.CharField(max_length=30)),
                ('contents', models.TextField()),
                ('tag', models.TextField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]