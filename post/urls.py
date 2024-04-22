from django.urls import path
from post import views

urlpatterns = [
    path('', views.show),
    path('search', views.search),
]
