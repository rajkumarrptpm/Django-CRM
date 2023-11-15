from django.urls import path
from . import views


urlpatterns =[
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]