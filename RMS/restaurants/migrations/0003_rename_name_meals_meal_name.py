# Generated by Django 4.0.6 on 2022-08-02 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_rename_name_restaurants_restaurant_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='name',
            new_name='meal_name',
        ),
    ]