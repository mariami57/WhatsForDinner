from django.test import TestCase
from django.urls import reverse

from subscriber.models import Subscriber


class NewsletterFromTests(TestCase):

    def test_newsletter_signup_view_renders_success(self):
        response = self.client.get(reverse('newsletter'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Sign up')


    def test_submitting_valid_newsletter_form_creates_subscriber(self):
        response = self.client.post(reverse('newsletter'), {
            'name': 'Test User',
            'email': 'test@example.com'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Subscriber.objects.filter(email='test@example.com').exists())