from django.shortcuts import render

from .models import Ingredient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import IngredientCreateForm

from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

def menu(request):
    return render(request, "inventory/menu.html")




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




def purchases(request):
    return render(request, "inventory/purchases.html")