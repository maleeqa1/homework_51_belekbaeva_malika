from django.urls import path
from catapp.views import home, cat_info
urlpatterns = [
    path('',home),
    path('cat_info/', cat_info),
]