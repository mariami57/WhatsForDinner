from django import forms

from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields =  ['title', 'prep_time', 'cook_time', 'instructions', 'ingredients']

        labels = {
            'title': 'Recipe title:',
            'image': 'Upload Image:',
            'instructions': 'Instructions:',
            'ingredients': 'Ingredients:',
            'prep_time':'Prep time:',
            'cook_time': 'Cook time',
        }

        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 3,
                'cols': 50}),
            'ingredients': forms.Textarea(attrs={'rows': 3,
                'cols': 50}),
        }

        placeholder= {
            'instructions':'Add instructions here',
            'ingredients': 'One ingredient per line:\nSugar\nFlour\nMilk',
            'prep_time': 'Preparation time in minutes:',
            'cook_time': 'Cooking time in minutes'
        }

class RecipeCreateForm(RecipeBaseForm):
    pass

class RecipeUpdateForm(RecipeBaseForm):
    pass



