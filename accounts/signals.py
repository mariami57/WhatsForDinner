from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from WhatsForDinner import settings
from accounts.models import Profile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(pk=instance.pk, user=instance)

        send_mail(
            subject='Welcome to our community!',
            message="Thank you for registering on 'What`s for Dinner'! We are excited to have you on board.",
            from_email=settings.COMPANY_EMAIL,
            recipient_list=[instance.email],
        )


