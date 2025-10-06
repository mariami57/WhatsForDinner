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

class NewsletterSignUpView(TemplateView):
    template_name = 'common/newsletter-sign-up.html'

class GlobalSearchAPIView(APIView):
    def get(self,request):
        query = request.GET.get('q', '')

        results = []

        if query:
            filters = Q(user__username__icontains=query) | Q(title__icontains=query) | Q(ingredients__icontains=query)
        else:
            recipes = Recipe.objects.none()

        recipes = Recipe.objects.filter(filters)
        recipe_data = RecipeSerializer(recipes, many=True).data

        for item in recipe_data:
            results.append({
                "pk": item.get("pk"),
                "label1": item.get("title", ""),
                "label2": item.get("user", {}).get("username", "") if isinstance(item.get("user"), dict) else "",
                "label3": item.get("ingredients", ""),
                "url": f"/recipes/{item.get('pk')}/details"
            })

        return Response(results)



