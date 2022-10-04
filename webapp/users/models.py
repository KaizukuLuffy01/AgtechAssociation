import datetime
import uuid as uuid
from django.db import models
from django.contrib.auth.models import User

TYPE_OF_USER = ((1, "individual"),
                (2, "institution"))


# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserType(models.Model):
    role = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_type'


class ExtendedProfile(models.Model):
    """
    ExtendedProfile for user
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    startup_name = models.CharField(max_length=1500, null=True, blank=True)
    tagline = models.CharField(max_length=1500, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=1500, null=True, blank=True)
    segment = models.CharField(max_length=1500, null=True, blank=True)
    business_model = models.CharField(max_length=1500, null=True, blank=True)
    cin_number = models.CharField(max_length=1500, null=True, blank=True)
    registration_state = models.ForeignKey(States, null=True, blank=True, on_delete=models.SET_NULL)
    founder_name = models.CharField(max_length=500, null=True, blank=True)
    founder_email = models.EmailField(max_length=250, null=True, blank=True)
    lastyear_revenue = models.CharField(max_length=50, null=True, blank=True)
    funded_bootstrapped = models.BooleanField(default=False)
    tech_brief = models.TextField(null=True, blank=True)
    rewards_recognition = models.TextField(null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'extended_profile'


class Profile(models.Model):
    """
    Extended user model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    user_type = models.IntegerField(choices=TYPE_OF_USER)
    extended_profile = models.ForeignKey(ExtendedProfile, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'user_extended'
