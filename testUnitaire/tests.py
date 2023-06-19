from django.test import TestCase
from testUnitaire.models import Person


class SimpleCalcul(TestCase):
    def test_addition_simple(self):
        """Simple addition"""
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 + 2, 22)


class SimpleTestDB(TestCase):
    def setUp(self):
        Person.objects.create(first_name="jean", last_name="wick")

    def test_database(self):
        """Simple test database"""
        cereal_killeur = Person.objects.get(first_name="jean")
        self.assertEqual(cereal_killeur.last_name, "wicked")
