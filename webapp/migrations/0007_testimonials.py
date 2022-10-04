# Generated by Django 3.2 on 2022-09-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20220928_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Testimonial/')),
                ('title', models.CharField(max_length=100)),
                ('test_type', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'agtech_testimonial',
            },
        ),
    ]
