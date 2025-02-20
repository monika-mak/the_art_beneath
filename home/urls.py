from django.urls import path
from . import views
from .views import artist_detail

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('artist/', artist_detail, name='artist_detail'),
]
