from django.contrib.auth import get_user_model
from django.test import TestCase

from recipes.models import Recipe

UserModel = get_user_model()

class RecipeModelTests(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(username='chef', password='pass123')
        self.recipe = Recipe.objects.create(
        user=self.user,
        title='Pasta Carbonara',
        instructions='Fry the pancetta and boil the pasta',
        ingredients='pasta, eggs, bacon',
        prep_time=10,
        cook_time=10,
        servings=2,
    )

    def test_string_representation_returns_true(self):
        self.assertEqual(str(self.recipe), 'Pasta Carbonara')

    def test_total_time_field_returns_true(self):
        self.assertEqual(self.recipe.total_time, 20)

