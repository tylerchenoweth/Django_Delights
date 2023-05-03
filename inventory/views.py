from django.shortcuts import render

from .models import MenuItem, Ingredient, Purchases

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import MenuItemCreateForm, IngredientCreateForm, PurchasesCreateForm

from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")



class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    success_url = reverse_lazy("inventory")
    template_name = "inventory/add_menuitem.html"

class MenuItemUpdate(UpdateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    success_url = reverse_lazy("inventory")
    template_name = "inventory/update_menuitem.html"    

class MenuItemDelete(DeleteView):
    model = MenuItem
    form_class = MenuItemCreateForm
    #success_url = reverse_lazy("inventory")
    success_url = "/inventory/inventory"
    template_name = "inventory/delete_menuitem.html"




class InventoryList(ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"

class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    success_url = reverse_lazy("inventory")
    template_name = "inventory/add_ingredient.html"

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientCreateForm
    success_url = reverse_lazy("inventory")
    template_name = "inventory/update_ingredient.html"    

class IngredientDelete(DeleteView):
    model = Ingredient
    form_class = IngredientCreateForm
    #success_url = reverse_lazy("inventory")
    success_url = "/inventory/inventory"
    template_name = "inventory/delete_ingredient.html"




#def purchases(request):
#   return render(request, "inventory/purchases.html")

class PurchasesList(ListView):
    model = Purchases
    template_name = "inventory/purchases.html"

class PurchasesCreate(CreateView):
    model = Purchases
    form_class = PurchasesCreateForm
    success_url = reverse_lazy("purchases")
    template_name = "inventory/add_purchases.html"

class PurchasesUpdate(UpdateView):
    model = Purchases
    form_class = PurchasesCreateForm
    success_url = reverse_lazy("purchases")
    template_name = "inventory/update_purchases.html"    

class PurchasesDelete(DeleteView):
    model = Purchases
    form_class = PurchasesCreateForm
    #success_url = reverse_lazy("inventory")
    success_url = "/inventory/purchases"
    template_name = "inventory/delete_purchases.html"
    