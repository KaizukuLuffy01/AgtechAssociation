import datetime

from django.db import models


# Create your models here.

#todo: add help text for image sizes
class AboutUs(models.Model):
    """
    Model for AboutUs Page
    """
    image1 = models.ImageField(upload_to='AboutUs/', null=True, blank=True, help_text="")
    image2 = models.ImageField(upload_to='AboutUs/', null=True, blank=True, help_text="")
    title = models.CharField(max_length=200, default='')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "aboutus"


class AgtechCategory(models.Model):
    """
    Model for AgtechCategories page
    """
    category_image = models.ImageField(upload_to='AgtechCat/', null=True, blank=True, help_text="")
    title = models.CharField(max_length=100, default='')
    text = models.TextField(default='')

    class Meta:
        db_table = 'agtech_category'

class Testimonials(models.Model):
    """
    Model for testimonial
    """
    image = models.ImageField(upload_to='Testimonial/', null=True, blank=True, help_text="")
    title = models.CharField(max_length=100)
    test_type = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        db_table = 'agtech_testimonial'

class WhyChooseUs(models.Model):
    """
    Model for why choose us
    """
    text = models.CharField(max_length=200,default='')
    number = models.IntegerField(default=0)

    class Meta:
        db_table = 'why_choose_us'

class LatestNews(models.Model):
    """
    Model for latest news
    """
    image = models.ImageField(upload_to='LatestNews/', null=True, blank=True, help_text="370X318")
    title = models.CharField(max_length=100,default='')
    text = models.TextField()
    timestamp = models.DateField(default=datetime.date.today())

    class Meta:
        db_table = 'latest_news'