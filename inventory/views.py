from django.shortcuts import render, get_object_or_404

from .models import MenuItem, Ingredient, RecipeRequirement, Purchases

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .forms import MenuItemCreateForm, IngredientCreateForm, PurchasesCreateForm, RecipeRequirementCreateForm

from django.urls import reverse_lazy

from django.forms import formset_factory



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
    template_name = "inventory/add_menuitem.html"

    def get_success_url(self):
        return reverse_lazy('reciperequirementcreate', kwargs={'pk': self.object.pk})


class MenuItemUpdate(UpdateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    success_url = reverse_lazy("menu")
    template_name = "inventory/update_menuitem.html"    

class MenuItemDelete(DeleteView):
    model = MenuItem
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
    #success_url = reverse_lazy("inventory")
    success_url = "/inventory/ingredient"
    template_name = "inventory/delete_ingredient.html"

class IngredientInMenuItems(ListView):
    model = RecipeRequirement
    template_name = "inventory/ingredient_in_menuitems.html"
    context_object_name = 'RR'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        url_pk = self.kwargs['pk']
        title = Ingredient.objects.get(pk=url_pk)

        context['url_pk'] = url_pk
        context['title'] = title

        return context

#def purchases(request):
#   return render(request, "inventory/purchases.html")

class PurchasesList(ListView):
    model = Purchases
    template_name = "inventory/purchases.html"

    #def get_queryset(self):
    #    return Purchases.objects.order_by('-timestamp')[:3]
    
    
from django.http import HttpResponseRedirect 
from django.http import HttpResponse

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


from django.db.models import F 

class PurchasesDelete(DeleteView):
    model = Purchases
    success_url = reverse_lazy("purchases")
    template_name = "inventory/delete_purchases.html"

    def post(self, request, *args, **kwargs):
        #add_back = form.cleaned_data['confirm_checkbox']
        #add_back = self.kwargs.get('confirm_checkbox')
        
        add_back = request.POST.get('add_ingredients_back') == 'checked'

        # add ingredients back if checkbox is checked
        if add_back:
            # Get the purchase object to be deleted
            purchaseToBeDeleted = self.get_object()

            # loop through the ingredients of the Recipe Requirement for the purchase
            for r in RecipeRequirement.objects.filter(menu_item=purchaseToBeDeleted.menu_item_id):
                
                # get the particular ingredient object from that recipe requirement
                ingredient_object = Ingredient.objects.get( pk=r.ingredient.pk ) 

                # add the recipe requirements back into the inventory
                Ingredient.objects.filter(
                    pk=r.ingredient.pk
                ).update(
                    quantity=F('quantity') + r.quantity
                )

        return super().post(request, *args, **kwargs)


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

from math import ceil

def round_up_to_two_decimal_places(num):
    return ( ceil( num * 100 ) / 100 )


class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        menu_item_cost = 0
        menu_item_price = 0

        # Get the PK for the current URL
        url_pk = self.kwargs['pk']
        title = Ingredient.objects.get(pk=url_pk)

        # Add up the cost of all the ingredients
        for r in RecipeRequirement.objects.filter(menu_item=url_pk):
            menu_item_cost += ( r.ingredient.unit_price * r.quantity )

        for m in MenuItem.objects.filter(pk=url_pk):
            menu_item_price = m.price
            break

        # Get cost and price of the menu item
        menu_item_cost = round_up_to_two_decimal_places( menu_item_cost )
        menu_item_price = round_up_to_two_decimal_places( menu_item_price )

        # round the decimals to the nearest two decimal points
        #   and calculate the menu item profite
        menu_item_cost = round( menu_item_cost, 2 )
        menu_item_price = round( menu_item_price, 2 )
        menu_item_profit = round( menu_item_price - menu_item_cost, 2 )

        context['url_pk'] = url_pk
        context['title'] = title        
        context['ingredients'] = RecipeRequirement.objects.filter(menu_item=url_pk)
        context['menu_item_instance'] = MenuItem.objects.get(pk=url_pk)
        context['menu_item_cost'] = menu_item_cost
        context['menu_item_price'] = menu_item_price
        context['menu_item_profit'] = menu_item_profit

        return context



RecipeRequirementFormset = formset_factory(RecipeRequirementCreateForm, extra=5, max_num=5)

class RecipeRequirementCreate(FormView):
    model = RecipeRequirementFormset
    form_class = RecipeRequirementFormset
    template_name = "inventory/add_reciperequirement.html"

    def get_success_url(self):
        return reverse_lazy('reciperequirement', args=[ self.kwargs['pk'] ] )

    def form_valid(self, form):
        formset_data = self.request.POST.get('formset')

        MenuItemObject = MenuItem.objects.get( pk=self.kwargs['pk'] )

        print( MenuItemObject )

        for f in form.cleaned_data:

            # This will check if the form is blank
            if( f.keys() ):
                if( RecipeRequirement.objects.filter(menu_item=MenuItemObject, ingredient=f['ingredient']).exists() ):
                    pass 
                else:
                    RecipeRequirement.objects.create(
                        menu_item = MenuItemObject,
                        ingredient = f['ingredient'],
                        quantity = f['quantity']
                    )



        """for f in formset_data:
            print(f)
        print("\n\n")

        instances = []
        for data in formset_data:
            form = self.form_class(data=data)
            if form.is_valid():
                instance = form.save(commit=False)
                # Additional processing or instance handling if needed
                instances.append(instance)
        
        if instances:
            print("\n\nSOMETHING HERERERER\n\n")
            RecipeRequirement.objects.bulk_create(instances)
        
        """

        return super().form_valid(form)

class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementCreateForm
    #success_url = reverse_lazy("menu")
    template_name = "inventory/update_reciperequirement.html" 

    def get_success_url(self):
        menu_item_obj = RecipeRequirement.objects.get( id=self.kwargs['pk'] )
        menu_item_id = menu_item_obj.menu_item_id
        return reverse_lazy('reciperequirement', args= [ menu_item_id ] )

class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    #success_url = reverse_lazy("menu")
    template_name = "inventory/delete_reciperequirement.html"  

    def get_success_url(self):
        menu_item_obj = RecipeRequirement.objects.get( id=self.kwargs['pk'] )
        menu_item_id = menu_item_obj.menu_item_id
        return reverse_lazy('reciperequirement', args= [ menu_item_id ] )    