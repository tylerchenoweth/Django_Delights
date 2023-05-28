from django.shortcuts import render, get_object_or_404

from .models import MenuItem, Ingredient, RecipeRequirement, Purchases

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import MenuItemCreateForm, IngredientCreateForm, RecipeRequirementCreateForm, PurchasesCreateForm 

from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

def details(request):
    #all_requirements = RecipeRequirement.objects.all()
    #context = {"all_requirements" : all_requirements }
    return render(request, 'inventory/details.html' )


class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    success_url = reverse_lazy("menu")
    template_name = "inventory/add_menuitem.html"

class MenuItemUpdate(UpdateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    success_url = reverse_lazy("menu")
    template_name = "inventory/update_menuitem.html"    

class MenuItemDelete(DeleteView):
    model = MenuItem
    form_class = MenuItemCreateForm
    #success_url = reverse_lazy("inventory")
    success_url = "/inventory/menu"
    template_name = "inventory/delete_menuitem.html"




class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient.html"

class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    success_url = reverse_lazy("ingredient")
    template_name = "inventory/add_ingredient.html"

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientCreateForm
    success_url = reverse_lazy("ingredient")
    template_name = "inventory/update_ingredient.html"    

class IngredientDelete(DeleteView):
    model = Ingredient
    form_class = IngredientCreateForm
    #success_url = reverse_lazy("inventory")
    success_url = "/inventory/ingredient"
    template_name = "inventory/delete_ingredient.html"




#def purchases(request):
#   return render(request, "inventory/purchases.html")

class PurchasesList(ListView):
    model = Purchases
    template_name = "inventory/purchases.html"

    #def get_queryset(self):
    #    return Purchases.objects.order_by('-timestamp')[:3]
    
    
        

class PurchasesCreate(CreateView):
    model = Purchases
    form_class = PurchasesCreateForm
    success_url = reverse_lazy("purchases")
    template_name = "inventory/add_purchases.html"

    #def form_valid(self, form):
    #    form.instance.amount_paid = form.instance.menu_item.price
    #    return super().form_valid(form)

    # this will add the amount_paid to the database automatically
    def form_valid(self, form):
        menu_item = form.cleaned_data.get('menu_item')
        amount_paid = form.cleaned_data.get('amount_paid')
        if menu_item and amount_paid <= 0:
            form.instance.amount_paid = menu_item.price

        return super().form_valid(form)
    

    

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



class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement.html"

    print("a;lkdsjf;lksajdf;lksjad;flkjkf;sakssad")

    def details(request):
        #test = get_object_or_404( RecipeRequirement.objects.filter( menu_item=4 ) )
        #print( test )
        #return render(request, 'reciperequirement', {'test':test})
        return RecipeRequirement.objects.filter( menu_item=4 )