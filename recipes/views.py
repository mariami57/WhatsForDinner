from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from common.mixins import UserIsOwnerMixin
from recipes.forms import RecipeCreateForm, RecipeUpdateForm
from recipes.models import Recipe


# Create your views here.
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('all-recipes')
    template_name = 'recipes/create-recipe.html'


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/all-recipes.html'


class RecipeEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'recipes/update-recipe.html'
    success_url = reverse_lazy('all-recipes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.user.pk == recipe.user.pk:
        recipe.delete()
        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('home')
    else:
        return HttpResponseForbidden('You are not allowed to delete this recipe')



