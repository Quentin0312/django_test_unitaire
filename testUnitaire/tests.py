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

# TODO: mettre en place newName, ...


class TestDb(TestCase):
    def getLastGame(self):
        return Games.objects.last()

    # TODO: rename
    def checkLastGame(self):
        name = self.getLastGame().name
        description = self.getLastGame().description
        price = self.getLastGame().price
        return {"name": name, "description": description, "price": price}

    # ----------------------------------------------------------------------------------

    # GET
    def test_api_client_get(self):
        # Insert in db
        Games.objects.create(name="orange", description="mandarine", price=2)

        # Test Db is working
        self.assertEqual(
            self.checkLastGame(),
            {"name": "orange", "description": "mandarine", "price": 2},
        )

        """API Client test GET"""
        response = self.client.get("/games/")

        # Status
        self.assertEquals(response.status_code, 200)

        # Response content
        self.assertEqual(
            json.loads(response.content),
            [
                {
                    "id": self.getLastGame().id,
                    "name": self.checkLastGame()["name"],
                    "description": self.checkLastGame()["description"],
                    "price": self.checkLastGame()["price"],
                }
            ],
        )

    # POST
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

        # Response content
        self.assertEqual(
            json.loads(response.content),
            {
                "id": self.getLastGame().id,  # TODO:
                "name": "rubix cube",
                "description": "diamant",
                "price": 2500,
            },
        )

        # Db content
        self.assertEqual(self.getLastGame().name, "rubix cube")
        self.assertEqual(self.getLastGame().description, "diamant")
        self.assertEqual(self.getLastGame().price, 2500)
