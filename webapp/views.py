from django.shortcuts import render
from django.views import View
from .utils import normalize_testimonial
from .models import AboutUs, AgtechCategory, WhyChooseUs, LatestNews, Testimonials



# Create your views here.

class HomeView(View):
    template_name = 'webapp/home.html'

    def get(self, request, *args, **kwargs):
        about_us = AboutUs.objects.last()
        agtech_cat = AgtechCategory.objects.all()
        why_choose_us = WhyChooseUs.objects.all().order_by('-id')[:4]
        latest_news = LatestNews.objects.all().order_by('-id')[:3]
        testimonials = Testimonials.objects.all()

        if not testimonials.count() % 2 == 0:
            testimonials = testimonials[:testimonials.count() - 1]

        normalized_testimonials = normalize_testimonial(testimonials)
        context = {'about_us': about_us, 'agtech_cat': agtech_cat,
                   'why_choose_us': why_choose_us, 'latest_news': latest_news,
                   'testimonials': normalized_testimonials, 't_count': len(normalized_testimonials)}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
