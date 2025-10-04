from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from accounts.forms import WebUserCreationForm, ProfileEditForm
from accounts.models import Profile
from common.mixins import UserIsOwnerMixin

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

class ProfileDetails(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'


class ProfileUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'


    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk':self.object.user.pk})

