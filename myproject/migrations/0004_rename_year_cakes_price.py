# Generated by Django 3.2.12 on 2022-03-01 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_rename_movies_cakes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cakes',
            old_name='year',
            new_name='price',
        ),
    ]
