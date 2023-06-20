import json
from django.test import TestCase
from testUnitaire.models import Games

# https://www.django-rest-framework.org/api-guide/testing/
# https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python


class TestDb(TestCase):
    def getLastGameItem(self):
        return Games.objects.last()

    def assertWithLastGameItem(self, name, description, price):
        self.assertEqual(self.getLastGameItem().name, name)
        self.assertEqual(self.getLastGameItem().description, description)
        self.assertEqual(self.getLastGameItem().price, price)

    def setUp(self):
        # Insert in db
        Games.objects.create(name="orange", description="mandarine", price=2)

        # Test if Db is working
        self.assertWithLastGameItem("orange", "mandarine", 2)

    # ----------------------------------------------------------------------------------

    # GET
    def test_api_get(self):
        """API test GET"""
        response = self.client.get("/games/")

        # Status
        self.assertEquals(response.status_code, 200)

        # Response content
        self.assertEqual(
            json.loads(response.content),
            [Games.objects.values().last()],
        )

    # POST
    def test_api_post(self):
        new_name = "rubix cube"
        new_description = "diamant"
        new_price = 2500

        """API test POST"""
        response = self.client.post(
            "/games/",
            {
                "name": new_name,
                "description": new_description,
                "price": new_price,
            },
            content_type="application/json",
        )
        # Status code
        self.assertEquals(response.status_code, 201)

        # Response content
        self.assertEqual(json.loads(response.content), Games.objects.values().last())

        # Db content
        self.assertWithLastGameItem(new_name, new_description, new_price)

    # PUT
    def test_api_put(self):
        new_name = "nouveau jouet"
        new_description = "interdit"
        new_price = 100

        """API test PUT"""
        response = self.client.put(
            f"/games/{self.getLastGameItem().id}/",
            {
                "name": new_name,
                "description": new_description,
                "price": new_price,
            },
            content_type="application/json",
        )

        # Status code
        self.assertEquals(response.status_code, 200)

        # Response content
        self.assertEquals(json.loads(response.content), Games.objects.values().last())

        # Db content
        self.assertWithLastGameItem(new_name, new_description, new_price)

    # DELETE
    def test_api_delete(self):
        response = self.client.delete(f"/games/{self.getLastGameItem().id}/")

        # Status code
        self.assertEqual(response.status_code, 204)

        # Db content
        self.assertEqual(Games.objects.count(), 0)
