from django.urls import path
from . import views


app_name = 'hsapp'
urlpatterns = [
    path('farmer_list/', views.FarmerList.as_view(), name='farmer_list'),
]