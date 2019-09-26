from django.urls import path
from . import views


app_name = 'hsapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dealer_info/', views.DealerInfo.as_view(), name='dealer_info'),
    path('farmer_list/', views.FarmerList.as_view(), name='farmer_list'),
    path('farmer_list/search_results/', views.SearchResultsView.as_view(), name='search_results_list'),
    path('farmer_list/search_test/', views.search_test, name='search_test'),
    path('create_farmer/', views.CreateNewFarmer.as_view(), name='create_farmer'),
    path('upload/', views.upload, name='upload'),
]

