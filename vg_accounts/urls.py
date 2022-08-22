from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='vg_accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='vg_accounts/logout.html'), name='logout'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('favorite/<str:title>/', views.favorite, name='favorite'),
]