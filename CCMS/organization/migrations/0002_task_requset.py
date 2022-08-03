# Generated by Django 4.0.6 on 2022-08-03 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cpmpany')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.service')),
            ],
        ),
        migrations.CreateModel(
            name='Requset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cpmpany')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.service')),
            ],
        ),
    ]