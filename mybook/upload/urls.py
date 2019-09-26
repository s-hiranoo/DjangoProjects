from django.urls import path
from . import views

app_name='upload'
urlpatterns = [
    path('load_csv', views.load_csv, name='load_csv'),
]
