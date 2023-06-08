from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    #path("<pk>/details", views.details, name="details"),

    path("menu", views.MenuItemList.as_view(), name="menu"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("menuitem/<pk>/update", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("menuitem/<pk>/delete", views.MenuItemDelete.as_view(), name="menuitemdelete"),

    path("ingredient", views.IngredientList.as_view(), name="ingredient"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("ingredient/<pk>/update", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("ingredient/<pk>/delete", views.IngredientDelete.as_view(), name="ingredientdelete"),

    #path("purchases", views.purchases, name="purchases"),
    path("purchases", views.PurchasesList.as_view(), name="purchases"),
    path("purchases/create", views.PurchasesCreate.as_view(), name="purchasescreate"),
    path("purchases/<pk>/update", views.PurchasesUpdate.as_view(), name="purchasesupdate"),
    path("purchases/<pk>/delete", views.PurchasesDelete.as_view(), name="purchasesdelete"),
    path("purchases/create/error", views.PurchasesCreateError, name="purchasescreateerror"),
    
    #path("reciperequirement/<int:pk>", views.RecipeRequirementList.as_view(), name="reciperequirement"),
    path("reciperequirement/<int:pk>", views.reciperequirement, name="reciperequirement"),
    path("reciperequirement/create", views.RecipeRequirementCreate.as_view(), name="reciperequirementcreate"),
]