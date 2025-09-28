from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from ingredients.models import Ingredient
from recipes.forms import RecipeCreateForm
from recipes.models import Recipe


# Create your views here.
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('all-recipes')
    template_name = 'recipes/create-recipe.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        ingredients = self.request.POST.getlist('ingredients')
        for name in ingredients:
            ingredient, created = Ingredient.objects.get_or_create(name=name)
            self.object.ingredients.add(ingredient)
        return response


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/all-recipes.html'



