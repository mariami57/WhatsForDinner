from django.urls import reverse_lazy
from django.views.generic import CreateView

from recipes.forms import RecipeCreateForm
from recipes.models import Recipe


# Create your views here.
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('home')
    template_name = 'recipes/create-recipe.html'

