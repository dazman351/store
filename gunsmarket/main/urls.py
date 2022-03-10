from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path("info/", views.info, name="info"),
    path('register/', views.register, name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/<int:id>', views.user_profile, name='user_profile'),
    path('edit/<int:id>', views.edit_profile, name='edit_profile'),

]