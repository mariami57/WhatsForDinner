from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from WhatsForDinner.serializers import RecipeSerializer
from recipes.models import Recipe


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'

class AboutPageView(TemplateView):
    template_name = 'common/about.html'

class ContactsPageView(TemplateView):
    template_name = 'common/contacts.html'

class GlobalSearchAPIView(APIView):
    def get(self,request):
        query = request.GET.get('q', '')
        results = []

        if query:
            recipes = Recipe.objects.filter(
                Q(user__username__icontains=query) |
                Q(title__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(total_time__icontains=query)
            )

            recipe_data = RecipeSerializer(recipes, many=True).data
            for item in recipe_data:
                item['label1'] = item['title']
                item['label2'] = item['username']
                item['label3'] = item['ingredients']
                item['label4'] = item['total_time']
            results.extend(recipe_data)

        return Response(results)