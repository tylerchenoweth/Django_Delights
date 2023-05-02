from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu", views.menu, name="menu"),

    path("inventory", views.InventoryList.as_view(), name="inventory"),
    path("inventory/create", views.IngredientCreate.as_view(), name="inventorycreate"),
    path("inventory/<pk>/update", views.IngredientUpdate.as_view(), name="inventoryupdate"),
    path("inventory/<pk>/delete", views.IngredientDelete.as_view(), name="inventorydelete"),

    path("purchases", views.purchases, name="purchases"),
    
]