from django.urls import path
from .views import (
    register,
    user_login,
    admin_dashboard,
    my_problems,
    department_dashboard
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('my-problems/', my_problems, name='my_problems'),
    path(
        'department-dashboard/',
        department_dashboard,
        name='department_dashboard'
    ),
]