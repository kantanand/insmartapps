from django.test import TestCase
from django.contrib.auth.models import User
from datacenter.models import UserProfile
# Create your tests here.

class UserProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="kantanand.usk@gmail.com",email="kantanand.usk@gmail.com",first_name="kantanand")
        User.objects.create(username="premanand@gmail.com",email="premanand@gmail.com",first_name="premanand")

    def test_user_profile_exists(self):
        """Animals that can speak are correctly identified"""
        usk = User.objects.get(username="kantanand.usk@gmail.com")
        usp = User.objects.get(username="premanand@gmail.com")
        self.assertEqual(usk.first_name, 'kantanand')
        self.assertEqual(usp.first_name, 'premanand')