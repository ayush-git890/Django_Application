from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.regis, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('dashboard/', views.dash_board, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
]
