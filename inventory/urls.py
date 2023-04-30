from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu", views.menu, name="menu"),
    path("inventory", views.InventoryList.as_view(), name="inventory"),
    path("purchases", views.purchases, name="purchases"),
    
]