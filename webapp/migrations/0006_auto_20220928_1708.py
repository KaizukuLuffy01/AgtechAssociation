# Generated by Django 3.2 on 2022-09-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_agtechcategory_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='AboutUs/'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='AboutUs/'),
        ),
    ]