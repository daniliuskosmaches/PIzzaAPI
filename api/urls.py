from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, PizzaViewSet, ChefViewSet, IngredientViewSet, ReviewViewSet

# Роутер сам создаст пути типа /restaurants/ и /restaurants/{id}/
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'pizzas', PizzaViewSet, basename='pizza')
router.register(r'chefs', ChefViewSet, basename='chef')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]