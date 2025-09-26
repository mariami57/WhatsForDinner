from django import forms


class IngredientBaseForm(forms.ModelForm):
    class Meta:
        fields= '__all__'

        labels = {
            'name': 'Name:',
            'quantity': 'Quantity:',
        }

class IngredientCreateForm(IngredientBaseForm):
    pass

class IngredientUpdateForm(IngredientBaseForm):
    pass