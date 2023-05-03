from django import forms
from .models import MenuItem, Ingredient, Purchases

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        #fields = ("name", "quantity", "unit", "unit_price") 
        fields = "__all__"

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        #fields = ("name", "quantity", "unit", "unit_price") 
        fields = "__all__"

class PurchasesCreateForm(forms.ModelForm):
    class Meta:
        model = Purchases
        #fields = ("name", "quantity", "unit", "unit_price") 
        fields = "__all__"