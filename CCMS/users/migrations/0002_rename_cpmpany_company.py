# Generated by Django 4.0.6 on 2022-08-03 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cpmpany',
            new_name='Company',
        ),
    ]
