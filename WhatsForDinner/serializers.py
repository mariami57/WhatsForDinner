from rest_framework import serializers

from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Recipe
        fields = ['pk', 'title', 'ingredients', 'total_time', 'servings']

    def get_url(self, obj):
        return f'recipes/{obj.id}/details'

