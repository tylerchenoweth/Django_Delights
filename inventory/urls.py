from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    #path("<pk>/details", views.details, name="details"),

    path("menu", views.MenuItemList.as_view(), name="menu"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("menuitem/<int:pk>/update", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("menuitem/<int:pk>/delete", views.MenuItemDelete.as_view(), name="menuitemdelete"),

    path("ingredient", views.IngredientList.as_view(), name="ingredient"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("ingredient/<int:pk>/update", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("ingredient/<int:pk>/delete", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("ingredient/<int:pk>/menuitems", views.IngredientInMenuItems.as_view(), name="ingredientinmenuitems"),

    #path("purchases", views.purchases, name="purchases"),
    path("purchases", views.PurchasesList.as_view(), name="purchases"),
    path("purchases/create", views.PurchasesCreate.as_view(), name="purchasescreate"),
    path("purchases/<int:pk>/update", views.PurchasesUpdate.as_view(), name="purchasesupdate"),
    path("purchases/<int:pk>/delete", views.PurchasesDelete.as_view(), name="purchasesdelete"),
    path("purchases/create/error", views.PurchasesCreateError, name="purchasescreateerror"),
    
    #path("reciperequirement", views.RecipeRequirementList.as_view(), name="reciperequirement"),
    #path("reciperequirement/<int:pk>", views.RecipeRequirementList.as_view(), name="reciperequirement"),
    path("reciperequirement/<int:pk>/", views.RecipeRequirementList.as_view(), name="reciperequirement"),
    path("reciperequirement/create/<int:pk>/", views.RecipeRequirementCreate.as_view(), name="reciperequirementcreate"),
    path("reciperequirement/<int:pk>/update", views.RecipeRequirementUpdate.as_view(), name="reciperequirementupdate"),
    path("reciperequirement/<int:pk>/delete", views.RecipeRequirementDelete.as_view(), name="reciperequirementdelete"),
]