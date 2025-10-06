from django.conf import settings
from django.core.mail import send_mass_mail
from django.core.management import BaseCommand

from subscriber.models import Subscriber


class Command(BaseCommand):
    help = "Send a newsletter email to all subscribers"

    def add_arguments(self, parser):
        parser.add_argument(
            '--subject',
            type=str,
            help='Subject line for the newsletter',
            required=True
        )

        parser.add_argument(
            '--message',
            type=str,
            help='Body of the newsletter message',
            required=True
        )

    def handle(self, *args, **options):
        subject = options['subject']
        message = options['message']
        subscribers = Subscriber.objects.all()

        if not subscribers.exists():
            self.stdout.write(self.style.WARNING('No subscribers found.'))
            return

        messages = [
            (subject,message, settings.DEFAULT_FROM_EMAIL, [s.email])
            for s in subscribers
        ]

        send_mass_mail(messages, fail_silently=False)

        self.stdout.write(
            self.style.SUCCESS(f'Newsletter sent to {subscribers.count()} subscribers.')

        )