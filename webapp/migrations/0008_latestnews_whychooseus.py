# Generated by Django 3.2 on 2022-10-01 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='LatestNews/')),
                ('title', models.CharField(default='', max_length=100)),
                ('text', models.TextField()),
                ('timestamp', models.DateField(default=datetime.date)),
            ],
            options={
                'db_table': 'latest_news',
            },
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=200)),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'why_choose_us',
            },
        ),
    ]