from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from recipes.models import Recipe

UserModel = get_user_model()
class SearchAPITests(APITestCase):

    def setUp(self):
        self.user = UserModel.objects.create(username='chef', password='pass123')
        self.recipe1 = Recipe.objects.create(
            user=self.user,
            title='Spaghetti Bolognese',
            instructions = "Fry the beef and boil the pasta",
            ingredients='beef, tomato, pasta',
            prep_time=10,
            cook_time=30,
            servings=4,

        )
        self.recipe2 =Recipe.objects.create(
            user=self.user,
            title='Quick Salad',
            ingredients='lettuce, tomato, cucumber',
            instructions="Cut the veggies",
            prep_time=10,
            cook_time=0,
            servings=2,

        )

    def test_global_search_by_title(self):
        url= reverse('global-search')
        response = self.client.get(url, {'q':'Spaghetti'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Spaghetti' in r['label1'] for r in response.data))

