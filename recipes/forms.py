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

        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5,
                'cols': 40, 'placeholder': "Add instructions here"}),
            'ingredients': forms.Textarea(attrs={'rows': 5,
                'cols': 40,'placeholder': "One ingredient per line:\nSugar\nFlour\nMilk"})
        }

class RecipeCreateForm(RecipeBaseForm):
    pass

class RecipeUpdateForm(RecipeBaseForm):
    pass



