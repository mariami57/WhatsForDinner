from django import forms


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        exclude = ('ingredients',)

        labels = {
            'title': 'Recipe title:',
            'image': 'Upload Image:',
            'instructions': 'Instructions:',
        }

class RecipeCreateForm(RecipeBaseForm):
    pass

class RecipeUpdateForm(RecipeBaseForm):
    pass



