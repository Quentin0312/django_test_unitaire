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

    # TODO: rename & refactor
    def checkLastGame(self):
        lastGame = self.getLastGame()
        return {
            "name": lastGame.name,
            "description": lastGame.description,
            "price": lastGame.price,
        }

    def setUp(self):
        # Insert in db
        Games.objects.create(name="orange", description="mandarine", price=2)

        # Test Db is working
        self.assertEqual(
            self.checkLastGame(),
            {"name": "orange", "description": "mandarine", "price": 2},
        )

    # ----------------------------------------------------------------------------------

    # GET
    def test_api_get(self):
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
    def test_api_post(self):
        """API Client test POST"""
        response = self.client.post(
            "/games/",
            {
                "name": "rubix cube",
                "description": "diamant",
                "price": 2500,
            },
            content_type="application/json",
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

    # PUT
    def test_api_put(self):
        response = self.client.put(
            f"/games/{self.getLastGame().id}/",
            {
                "name": "nouveau jouet",
                "description": "interdit",
                "price": 100,
            },
            content_type="application/json",
        )

        # Status code
        self.assertEquals(response.status_code, 200)

        # Response content
        self.assertEquals(
            json.loads(response.content),
            {
                "id": self.getLastGame().id,  # TODO:
                "name": "nouveau jouet",
                "description": "interdit",
                "price": 100,
            },
        )

        # Db content
        self.assertEqual(self.getLastGame().name, "nouveau jouet")
        self.assertEqual(self.getLastGame().description, "interdit")
        self.assertEqual(self.getLastGame().price, 100)

    # DELETE

    def test_api_delete(self):
        print("Games.objects.all()", Games.objects.all())
        response = self.client.delete(f"/games/{self.getLastGame().id}/")

        # Status code
        self.assertEqual(response.status_code, 204)

        # Db content
        self.assertEqual(Games.objects.count(), 0)
