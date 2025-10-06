from django.urls import path

from subscriber.views import NewsletterSubscriberView

urlpatterns = [
    path('subscribe/', NewsletterSubscriberView.as_view(), name='newsletter')
]