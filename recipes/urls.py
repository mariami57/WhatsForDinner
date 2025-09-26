from django.urls import path

from recipes.views import RecipeCreateView

urlpatterns = [
    path('create-recipe/', RecipeCreateView.as_view(), name='create-recipe'),

]