from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from common.mixins import UserIsOwnerMixin
from recipes.forms import RecipeCreateForm, RecipeUpdateForm
from recipes.models import Recipe


# Create your views here.
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('all-recipes')
    template_name = 'recipes/create-recipe.html'

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super().form_valid(form)


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

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'

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
        return redirect('all-recipes')
    else:
        return HttpResponseForbidden('You are not allowed to delete this recipe')


class MyRecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/my-recipes.html'
    context_object_name = 'my_recipes_list'

    def get_queryset(self):
        return Recipe.objects.filter(user = self.request.user)

@login_required
@require_POST
def toggle_favourite(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.user in recipe.favourited_by.all():
        recipe.favourited_by.remove(request.user)
        return JsonResponse({'favourited': False})
    else:
        recipe.favourited_by.add(request.user)
        return JsonResponse({'favourited': True})

class MyFavouriteRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name= 'recipes/favourite-recipes.html'
    context_object_name='favourite_recipes'

    def get_queryset(self):
        return self.request.user.favourite_recipes.all()


class RecipeIndexView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = Recipe.objects.all().order_by('title')
        letter = self.request.GET.get('letter')
        if letter:
            queryset = queryset.filter(title__istartswith=letter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letter'] = [chr(i) for i in range(65,91)]
        context['active_letter'] = self.request.GET.get('letter', '')
        return context