from django.test import TestCase
from testUnitaire.models import Person

# Create your tests here.

# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')


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
