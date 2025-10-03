from django import forms

from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields =  ['title', 'prep_time', 'cook_time', 'instructions', 'ingredients', 'image', 'servings']

        labels = {
            'title': 'Recipe title:',
            'image': 'Upload Image:',
            'instructions': 'Instructions:',
            'ingredients': 'Ingredients:',
            'prep_time':'Prep time:',
            'cook_time': 'Cooking time:',
            'servings': 'Servings'

        }

        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5,
                'cols': 40, 'placeholder':'Add instructions here'}),
            'ingredients': forms.Textarea(attrs={'rows': 5,
                'cols': 40, 'placeholder':'One ingredient per line:\nSugar\nFlour\nMilk'}),
            'prep_time': forms.NumberInput(attrs= {
                'placeholder':'In minutes'
            }),
            'cook_time': forms.NumberInput(attrs= {
                'placeholder':'In minutes'}),
            'servings':forms.NumberInput(attrs= {
                'placeholder':'Number of servings'}),
        }



class RecipeCreateForm(RecipeBaseForm):
    pass

class RecipeUpdateForm(RecipeBaseForm):
    pass



