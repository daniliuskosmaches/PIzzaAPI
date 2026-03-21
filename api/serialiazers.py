from rest_framework import serializers
from .models import *


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    ingredient_ids = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(),
        many=True,
        write_only=True,
        source='ingredients'
    )

    class Meta:
        model = Pizza
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'restaurant_name', 'rating', 'text']

class ChefSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Chef
        fields = ['id', 'name', 'restaurant_name']


class RestaurantSerializer(serializers.ModelSerializer):
    chef = ChefSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'chef']