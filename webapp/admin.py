from django.contrib import admin
from .models import AboutUs,AgtechCategory,Testimonials,WhyChooseUs,LatestNews

# Register your models here.


admin.site.register(Testimonials)
admin.site.register(AboutUs)
admin.site.register(AgtechCategory)
admin.site.register(WhyChooseUs)
admin.site.register(LatestNews)