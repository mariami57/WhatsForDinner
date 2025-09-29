from django.urls import path
from common.views import HomeView, AboutPageView, ContactsPageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('contacts/', ContactsPageView.as_view(), name='contacts')
]