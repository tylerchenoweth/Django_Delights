from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

def menu(request):
    return render(request, "inventory/menu.html")

def inventory(request):
    return render(request, "inventory/inventory.html")

def purchases(request):
    return render(request, "inventory/purchases.html")