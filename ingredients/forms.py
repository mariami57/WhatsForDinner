from django import forms

from ingredients.models import Ingredient


class IngredientBaseForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields= '__all__'

        labels = {
            'name': 'Name:',
            'quantity': 'Quantity:',
        }

class IngredientCreateForm(IngredientBaseForm):
    pass

class IngredientUpdateForm(IngredientBaseForm):
    pass