# Generated by Django 4.1.5 on 2023-03-17 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_Name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carousel_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='Carousel')),
                ('image_2', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='Carousel')),
                ('image_3', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='Carousel')),
            ],
        ),
        migrations.CreateModel(
            name='Categoriys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Image', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='ProductsImage/Catagory_Image')),
                ('Category_Name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='ProductsImage/Laptop_Image')),
                ('Image_1', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='ProductsImage/Laptop_Image')),
                ('Image_2', models.ImageField(default='ProductsImage/Catagory_Image/CatagoryDefultImage.png', upload_to='ProductsImage/Laptop_Image')),
                ('Product_Name', models.TextField(blank=True, max_length=300, null=True)),
                ('Product_Model', models.TextField(blank=True, max_length=300, null=True)),
                ('Regular_Price', models.IntegerField(default=0)),
                ('Special_Price', models.IntegerField(default=0)),
                ('Warranty', models.CharField(max_length=50)),
                ('Product_Details', models.TextField(max_length=1000)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.categoriys')),
                ('Product_Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total', models.FloatField(default=0.0)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]