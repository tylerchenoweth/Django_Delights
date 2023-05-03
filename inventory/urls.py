from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("menu", views.MenuItemList.as_view(), name="menu"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("menuitem/<pk>/update", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("menuitem/<pk>/delete", views.MenuItemDelete.as_view(), name="menuitemdelete"),

    path("inventory", views.InventoryList.as_view(), name="inventory"),
    path("inventory/create", views.IngredientCreate.as_view(), name="inventorycreate"),
    path("inventory/<pk>/update", views.IngredientUpdate.as_view(), name="inventoryupdate"),
    path("inventory/<pk>/delete", views.IngredientDelete.as_view(), name="inventorydelete"),

    #path("purchases", views.purchases, name="purchases"),
    path("purchases", views.PurchasesList.as_view(), name="purchases"),
    path("purchases/create", views.PurchasesCreate.as_view(), name="purchasescreate"),
    path("purchases/<pk>/update", views.PurchasesUpdate.as_view(), name="purchasesupdate"),
    path("purchases/<pk>/delete", views.PurchasesDelete.as_view(), name="purchasesdelete"),
    
]