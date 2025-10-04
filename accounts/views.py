from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import WebUserCreationForm



UserModel = get_user_model()
# Create your views here.
class RegisterView(CreateView):
    model = UserModel
    form_class=WebUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
    #Uses signal to create a profile for the user

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully registered! Please log in.')
        return super().form_valid(form)

class ProfileDetails(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

