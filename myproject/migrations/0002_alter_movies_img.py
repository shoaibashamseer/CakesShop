# Generated by Django 3.2.12 on 2022-02-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]