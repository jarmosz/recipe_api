from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """tEST CERAING A NEW USER IS SUCCESSFULL"""

    def test_create_user_with_email_successfull(self):
        email = "asd@asd.pl"
        password = "Haslo123"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test normalizing user email"""
        email = "test@TadfhaafGRGS.pl"
        user = get_user_model().objects.create_user(email, "test123123123123")

        self.assertEqual(email.lower(), user.email)

    def test_new_user_invalid_email(self):
        """Test user creating with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test42837492374923749")

    def test_create_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser("test@asd.com", "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
