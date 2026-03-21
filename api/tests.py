from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Restaurant, Chef, Pizza, Ingredient


class PizzaRestaurantIntegrationTests(APITestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Pizza",
            address="Almaty Street 1"
        )
        self.chef = Chef.objects.create(
            name="Gordon Ramzaev",
            restaurant=self.restaurant
        )
        self.ingredient = Ingredient.objects.create(name="Cheese")

        self.pizza = Pizza.objects.create(
            name="Margarita",
            cheese_type="Mozzarella",
            dough_thickness="thin",
            secret_ingredient="Love",
            restaurant=self.restaurant
        )
        self.pizza.ingredients.add(self.ingredient)

    def test_get_restaurant_list(self):
        url = reverse('restaurant-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Pizza")

    def test_get_restaurant_menu(self):
        url = reverse('restaurant-menu', kwargs={'pk': self.restaurant.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['restaurant'], self.restaurant.name)
        self.assertTrue(len(response.data['menu']) > 0)
        self.assertEqual(response.data['menu'][0]['name'], "Margarita")

    def test_create_review_validation(self):

        url = reverse('review-list')
        data = {
            "restaurant": self.restaurant.id,
            "text": "Too good!",
            "rating": 10
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pizza_ingredients_relation(self):
        url = reverse('pizza-detail', kwargs={'pk': self.pizza.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ingredients'][0]['name'], "Cheese")

    def test_chef_one_to_one_constraint(self):
        with self.assertRaises(Exception):
            Chef.objects.create(name="Second Chef", restaurant=self.restaurant)