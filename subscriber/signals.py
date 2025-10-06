from django.db.models.signals import post_save
from django.dispatch import receiver

from subscriber.models import Subscriber


@receiver(post_save, sender=Subscriber)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Our Newsletter!"
        message = (
            f"Hi,\n\n"
            f"Thank you for subscribing to our newsletter! 🎉\n"
            f"You’ll receive occasional updates with recipes, tips, and more.\n\n"
            f"- The 'What`s for Dinner' Team"
        )
