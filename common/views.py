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
            filters = (
                Q(user__username__icontains=query) |
                Q(title__icontains=query) |
                Q(ingredients__icontains=query)

            )

            if query.isdigit():
                filters |= Q(total_time=int(query))

            recipes = Recipe.objects.filter(filters)
            recipe_data = RecipeSerializer(recipes, many=True).data
            for item in recipe_data:

                item['label1'] = item.get('title', '')
                item['label2'] = item['user']['username']
                item['label3'] = item.get('ingredients','')
                item['label4'] = item.get('total_time','')
            results.extend(recipe_data)

        return Response(results)