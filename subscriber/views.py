from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from subscriber.forms import SubscriberCreateForm
from subscriber.models import Subscriber


# Create your views here.
class NewsletterSubscriberView(CreateView):
    model = Subscriber
    form_class = SubscriberCreateForm
    template_name = 'subscriber/newsletter-sign-up.html'
    success_url = reverse_lazy('all-recipes')
    #Uses signal to make a user a subscriber

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully subscribed to our newsletter!')
        return super().form_valid(form)

