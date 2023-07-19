from django import forms
from .models import MenuItem, Ingredient, RecipeRequirement, Purchases

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem 
        fields = "__all__"

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class PurchasesCreateForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = "__all__"

class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ("ingredient", "quantity")    