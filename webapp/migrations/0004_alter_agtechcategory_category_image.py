# Generated by Django 3.2 on 2022-09-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_agtechcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agtechcategory',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]