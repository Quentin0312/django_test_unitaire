from django.test import TestCase
from testUnitaire.models import Person, Games


# class SimpleCalcul(TestCase):
#     def test_addition_simple(self):
#         """Simple addition"""
#         self.assertEqual(1 + 1, 2)
#         self.assertEqual(2 + 2, 22)


class SimpleTestDB(TestCase):
    def setUp(self):
        Person.objects.create(first_name="jean", last_name="wick")

    def test_database(self):
        """Simple test database"""
        cereal_killeur = Person.objects.get(first_name="jean")
        self.assertEqual(cereal_killeur.last_name, "wick")


class TestDb(TestCase):
    def setUp(self):
        Games.objects.create(name="yoyo", description="1,50m, or plaqué", price=50)

    def test_add_item(self):
        """Test database working"""
        game_added = Games.objects.get(name="yoyo")
        self.assertEqual(game_added.price, 50)
