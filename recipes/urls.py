from django.urls import path

from recipes.views import RecipeCreateView, RecipesListView

urlpatterns = [
    path('create-recipe/', RecipeCreateView.as_view(), name='create-recipe'),
    path('all-recipes/', RecipesListView.as_view(), name='all-recipes'),


]