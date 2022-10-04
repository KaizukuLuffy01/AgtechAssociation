# Generated by Django 3.2 on 2022-09-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_aboutus_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgtechCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='AgtechCat/')),
                ('title', models.CharField(default='', max_length=100)),
                ('text', models.TextField(default='')),
            ],
            options={
                'db_table': 'agtech_category',
            },
        ),
    ]
