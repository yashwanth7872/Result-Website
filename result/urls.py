from django.urls import path
from . import views

app_name='result'
urlpatterns = [
    path('',views.index,name='index'),
    path('fetch', views.fetch_result ,name='fetch_result'),
]