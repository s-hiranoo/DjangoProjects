from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'hsapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dealer_info/', views.DealerInfo.as_view(), name='dealer_info'),
    path('farmer_list/', views.FarmerList.as_view(), name='farmer_list'),
    path('farmer_list/search_results/', views.SearchResultsView.as_view(), name='search_results_list'),
    path('farmer_list/search_test/', views.search_test, name='search_test'),
    path('create_farmer/', views.CreateNewFarmer.as_view(), name='create_farmer'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('plant_list/', views.PlantList.as_view(), name='plant_list'),
    path('plant_detail/<int:pk>/', views.PlantDetail.as_view(), name='plant_detail'),
    path('company_list/', views.CompanyList.as_view(), name='company_list'),
    path('company_detail/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
]

