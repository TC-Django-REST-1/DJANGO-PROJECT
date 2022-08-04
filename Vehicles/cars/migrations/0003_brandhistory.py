# Generated by Django 4.0.6 on 2022-08-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_brand_last_revenue_billion'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('established_in', models.PositiveIntegerField()),
                ('origin', models.CharField(max_length=255)),
                ('founder', models.CharField(max_length=255)),
                ('headquarters', models.TextField()),
                ('last_revenue', models.DecimalField(decimal_places=2, max_digits=12)),
                ('year', models.PositiveIntegerField()),
                ('remarks', models.TextField(blank=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modification_date', models.DateField()),
            ],
        ),
    ]
