from django.urls import path, include
from .views import HomeView

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view()),
    path('user/', include('webapp.users.urls')),
]
