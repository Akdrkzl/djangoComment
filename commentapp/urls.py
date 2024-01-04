from django.urls import path
from .views import *

urlpatterns = [
    path('home/',index,name='index'),
    path('sil/',sil,name='sil')
]
