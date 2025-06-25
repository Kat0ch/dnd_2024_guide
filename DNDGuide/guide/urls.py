from .views import *
from django.urls import path

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add_class/', AddClass.as_view(), name='add_class'),
]
