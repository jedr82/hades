# Generated by Django 4.1 on 2022-08-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
