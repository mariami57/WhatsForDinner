from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from recipes.forms import RecipeCreateForm
from recipes.models import Recipe


# Create your views here.
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('all-recipes')
    template_name = 'recipes/create-recipe.html'


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/all-recipes.html'



