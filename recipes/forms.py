from django import forms

from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        labels = {
            'title': 'Recipe title:',
            'image': 'Upload Image:',
            'instructions': 'Instructions:',
            'ingredients': 'Ingredients:',
        }

class RecipeCreateForm(RecipeBaseForm):
    pass

class RecipeUpdateForm(RecipeBaseForm):
    pass



