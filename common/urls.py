from django.urls import path
from common.views import HomeView, AboutPageView, ContactsPageView, GlobalSearchAPIView, TimeSearchAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('api/search/', GlobalSearchAPIView.as_view(), name='global-search'),

    path('api/time-search/', TimeSearchAPIView.as_view(), name='time-search'),
]