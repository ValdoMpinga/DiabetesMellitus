# Generated by Django 4.0.5 on 2022-06-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
