# Generated by Django 4.0.5 on 2022-06-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticsample',
            name='sexo',
            field=models.TextField(choices=[('m', 'Masculino'), ('f', 'Feminino')], default='f'),
        ),
    ]