from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import WebUserCreationForm
from accounts.models import WebUser


# Create your views here.
class RegisterView(CreateView):
    model = WebUser
    form_class=WebUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
    #Uses signal to create a profile for the user

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully registered! Please log in.')
        return super().form_valid(form)

