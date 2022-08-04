# Generated by Django 3.2.14 on 2022-08-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('contactInfo', models.CharField(max_length=12)),
                ('bookedAt', models.DateField(default='2000-1-1')),
            ],
        ),
    ]