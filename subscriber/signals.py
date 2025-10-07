from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from WhatsForDinner import settings
from subscriber.models import Subscriber


@receiver(post_save, sender=Subscriber)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        user_name = instance.name if instance.name else "there"
        subject = "Welcome to Our Newsletter!"
        message = (
            f"Hi {user_name},\n\n"
            f"Thank you for subscribing to our newsletter! 🎉\n"
            f"You’ll receive occasional updates with recipes, tips, and more.\n\n"
            f"- The 'What`s for Dinner' Team"
        )
        send_mail(
            subject,
            message,
            from_email=settings.COMPANY_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
