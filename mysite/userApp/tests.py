from django.test import TestCase
from .models import User
# Create your tests here.

class UserTest(TestCase):
    def setup(self):
        """Setting up a student, organization, and admin to test"""
        User.objects.create(username="student_test_object", first_name="student", lastname="student", password="studenttest", email="student@test.com", is_staff=0, is_superuser=0)
        User.objects.create(username="organization_test_object", first_name="organization", lastname="organization", password="organizationtest", email="organization@test.com", is_staff=1, is_superuser=0)
        User.objects.create(username="admin_test_object", first_name="admin", lastname="admin", password="admintest", email="admin@test.com", is_staff=1, is_superuser=1)

    def test_student_users_can_view_post(self):
        """Only students and admins can return true"""
        s = User.objects.get(id=1)
        self.assertEqual(s.can_view_post(), True)
    
    def test_organization_users_can_view_post(self):
        """Only students and admins can return true"""
        o = User.objects.get(id=2)
        self.assertEqual(o.can_view_post(), False)

    def test_admin_users_can_view_post(self):
        """Only students and admins can return true"""
        a = User.objects.get(id=3)
        self.assertEqual(a.can_view_post(), True)