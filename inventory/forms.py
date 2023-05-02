from django import forms
from .models import Ingredient

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        #fields = ("name", "quantity", "unit", "unit_price") 
        fields = "__all__"

