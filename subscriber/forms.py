from django import forms

from subscriber.models import Subscriber


class SubscriberBaseForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ('date_subscribed',)
