from django.contrib import admin
from webapp.users.models import Profile,ExtendedProfile,States
from webapp.models import AboutUs,AgtechCategory

# Register your models here.

admin.site.register(Profile)
admin.site.register(ExtendedProfile)
admin.site.register(States)

