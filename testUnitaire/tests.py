import json
from django.test import TestCase
from testUnitaire.models import Games

# Possibiltés de tests: (pros and cons ?)
# - APIRequestFactory
# - APIClient
# - RequestsClient
# - CoreAPIClient
# - API Test cases
# - URLPatternsTestCase
# https://www.django-rest-framework.org/api-guide/testing/

# plans de tests à mettre en place

# reste à lire:
# https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python


class TestDb(TestCase):
    def setUp(self):
        Games.objects.create(name="yoyo", description="1,50m, or plaqué", price=50)

    def test_add_item(self):
        """Test database is working"""
        game_added = Games.objects.get(name="yoyo")
        self.assertEqual(game_added.price, 50)

    # API Client
    def test_api_client(self):
        """API Client test GET"""
        response = self.client.get("/games/")
        # TODO: compare json not strings
        self.assertEqual(
            json.loads(response.content),
            [
                {
                    "id": 1,
                    "name": "yoyo",
                    "description": "1,50m, or plaqué",
                    "price": 50.0,
                }
            ],
        )

    def test_api_client_post(self):
        """API Client test POST"""
        response = self.client.post(
            "/games/",
            {
                "name": "rubix cube",
                "description": "diamant",
                "price": 2500,
            },
        )

        self.assertEqual(
            json.loads(response.content),
            {
                "id": 2,
                "name": "rubix cube",
                "description": "diamant",
                "price": 2500,
            },
        )
