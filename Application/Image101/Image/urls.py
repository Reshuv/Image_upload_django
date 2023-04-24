from django.urls import path
from .views import image_view

urlpatterns = [
    path('image_view/', image_view, name='image_view'),
]