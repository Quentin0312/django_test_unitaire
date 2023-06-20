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
    def getLastGame(self):
        return Games.objects.last()

    def setUp(self):
        Games.objects.create(name="yoyo", description="1,50m, or plaqué", price=50)

    def test_add_item(self):
        """Test database is working"""

        self.assertEqual(self.getLastGame().name, "yoyo")
        self.assertEqual(self.getLastGame().description, "1,50m, or plaqué")
        self.assertEqual(self.getLastGame().price, 50)

    # API Client
    def test_api_client(self):
        """API Client test GET"""
        response = self.client.get("/games/")
        # TODO: compare json not strings
        self.assertEquals(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content),
            [
                {
                    "id": self.getLastGame().id,
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
        # Status code
        self.assertEquals(response.status_code, 201)

        # Content
        self.assertEqual(
            json.loads(response.content),
            {
                "id": self.getLastGame().id,
                "name": "rubix cube",
                "description": "diamant",
                "price": 2500,
            },
        )
        self.assertEqual(self.getLastGame().name, "rubix cube")
        self.assertEqual(self.getLastGame().description, "diamant")
        self.assertEqual(self.getLastGame().price, 2500)
