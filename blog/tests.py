from django.test import TestCase
from account.models import Account

class BlogPostTestCase(TestCase):
    def setUp(self):
        print("setUp Activity")
        Account.objects.create(email="dineshsingireddy@gmail.com", username="dineshsingireddy@gmail.com")

    def test_blogpost_info(self):
        print("Testing BlogPost Functionality")
        a1 = Account.objects.get()
        email = Account._meta.get_field('email').verbose_name
        self.assertEqual(email, 'dineshsingireddy@gmail.com')