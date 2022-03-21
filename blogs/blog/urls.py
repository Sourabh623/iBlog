from django.urls import path
from .views import home, post

urlpatterns = [
    path('home/', home),
    path('blog/<slug:url>', post),
]
