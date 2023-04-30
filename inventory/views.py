from django.shortcuts import render

from .models import Ingredient
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

def menu(request):
    return render(request, "inventory/menu.html")

class InventoryList(ListView):
    model = Ingredient
    #return render(request, "inventory/inventory.html")
    template_name = "inventory/inventory.html"

def purchases(request):
    return render(request, "inventory/purchases.html")