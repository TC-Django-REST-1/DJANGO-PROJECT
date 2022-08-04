# Generated by Django 4.0.6 on 2022-08-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_trainees_te_phone_alter_trainers_end_date_and_more'),
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='c_name',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='course',
            name='c_trainee',
            field=models.ManyToManyField(blank=True, to='Users.trainees'),
        ),
        migrations.AlterField(
            model_name='course',
            name='c_type',
            field=models.CharField(max_length=512),
        ),
    ]