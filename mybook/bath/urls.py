from django.urls import path
from . import views

app_name='bath'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:member_id>/done/', views.done, name='done'),
    path('reserve/', views.reserve, name='reserve'),
    path('login-user/', views.show_login_user, name='show_login_user'),
]
