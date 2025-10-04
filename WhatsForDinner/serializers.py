from rest_framework import serializers

from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'total_time', 'servings']

        def get_url(self, obj):
            return f'recipes/{obj.id}/details'

