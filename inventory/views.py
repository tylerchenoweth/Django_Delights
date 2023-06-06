from django.shortcuts import render, get_object_or_404

from .models import MenuItem, Ingredient, RecipeRequirement, Purchases

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import MenuItemCreateForm, IngredientCreateForm, PurchasesCreateForm#, RecipeRequirementCreateForm

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
    
    
from django.http import HttpResponseRedirect 

from django.contrib import messages

class SuccessMessageMixin:
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        return response
    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
        #return super().form_valid(form, request)

class PurchasesCreate(SuccessMessageMixin, CreateView):
    model = Purchases
    form_class = PurchasesCreateForm
    success_url = reverse_lazy("purchases")
    template_name = "inventory/add_purchases.html"

    #success_message = None

    # this will add the amount_paid to the database automatically
    def form_valid(self, form):
        
        menu_item = form.cleaned_data.get('menu_item')
        amount_paid = form.cleaned_data.get('amount_paid')
        menu_item_ID = menu_item.pk
  
        print("QUERY:")
        available_ingredient_qty = 0
        required_ingredient_qty = 0
        tuple_numbers = []

        # update the quantity of each ingredient
        for i in RecipeRequirement.objects.filter(menu_item=menu_item.pk):
            required_ingredient_qty = i.quantity
            for k in Ingredient.objects.filter(id=i.ingredient.pk):
                available_ingredient_qty = k.quantity
           
            print("Required QTY: ", required_ingredient_qty )
            print("Available QTY: ", available_ingredient_qty )

            tuple_numbers.append( [i.ingredient.pk, available_ingredient_qty, required_ingredient_qty] )

        allIngredientsAvailable = True

        for t in tuple_numbers:
            if( (t[1] - t[2]) < 0 or t[1] == 0 ):
                allIngredientsAvailable = False

        if( allIngredientsAvailable == True ):
            for t in tuple_numbers:
                Ingredient.objects.filter(id=t[0]).update(quantity=(t[1]-t[2]))
                print("DEDUCTING INGREDIENTS")

            print("\n\n\n")

            if menu_item and amount_paid <= 0:
                form.instance.amount_paid = menu_item.price

            #success_message = "Purchase Added Successfully!"
            return super().form_valid(form)
        else:
            return HttpResponseRedirect("./create/error")
            #success_message = "Not enough ingredients!"
            #return super().form_valid(form)

    

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

def PurchasesCreateError(request):
    return render(request, "inventory/add_purchase_error.html")

"""class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement.html"

    print("a;lkdsjf;lksajdf;lksjad;flkjkf;sakssad")

    def details(request):
        #test = get_object_or_404( RecipeRequirement.objects.filter( menu_item=4 ) )
        #print( test )
        #return render(request, 'reciperequirement', {'test':test})
        return RecipeRequirement.objects.filter( menu_item=4 )
"""

def reciperequirement(request, pk):

    menu_item_cost = 0
    menu_item_price = 0

    for r in RecipeRequirement.objects.filter(menu_item=pk):
        menu_item_cost += ( r.ingredient.unit_price * r.quantity )

    for m in MenuItem.objects.filter(pk=pk):
        menu_item_price = m.price
        break

    menu_item_profit = round( menu_item_price - menu_item_cost, 2 )

    context = { 
        "ingredients": RecipeRequirement.objects.filter(menu_item=pk),
        "menu_item_money": { 
            "menu_item_cost" : menu_item_cost, 
            "menu_item_price" : menu_item_price,
            "menu_item_profit" : menu_item_profit,
            }
        }

    return render(request, "inventory/reciperequirement.html", context)