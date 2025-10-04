from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

UserModel = get_user_model()

class WebUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields=('username', 'email')


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        widgets = {
            "bio_info": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us something about yourself"}),
        }

class ProfileEditForm(ProfileBaseForm):
    pass