from django.urls import path
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('admin-dashboard/', user_views.adminDashboard, name='admin_dashboard'),
]
