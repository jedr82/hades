# Generated by Django 4.1 on 2022-08-28 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Venta'),
        ),
    ]
