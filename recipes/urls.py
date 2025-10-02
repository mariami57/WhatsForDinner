from django.urls import path, include

from recipes import views
from recipes.views import RecipeCreateView, RecipesListView, RecipeEditView

urlpatterns = [
    path('create-recipe/', RecipeCreateView.as_view(), name='create-recipe'),
    path('all-recipes/', RecipesListView.as_view(), name='all-recipes'),

    path('<int:pk>/', include([
        path('update/', RecipeEditView.as_view(), name='update'),
        path('delete/', views.delete_recipe, name='delete'),
    ]))


]