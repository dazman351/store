from django.urls import path
from . import views

urlpatterns = [
    path('', views.guns, name="guns"),
    path('search/', views.search, name='search'),
    path('<int:id>', views.product_detail, name='description'),
]