from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from recipes.forms import RecipeCreateForm, RecipeUpdateForm
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


class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'recipes/update-recipe.html'
    success_url = reverse_lazy('all-recipes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        kwargs['request'] = self.request
        return kwargs




