from django.urls import path
from post import views

urlpatterns = [
    path('<slug:slug>', views.show),
    path('search', views.search),
]
