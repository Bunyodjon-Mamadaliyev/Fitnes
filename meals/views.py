from rest_framework import generics, permissions
from .models import Meal, MealFood, HealthMetrics
from .serializers import MealSerializer, MealFoodSerializer, HealthMetricsSerializer
from common.permissions import IsOwnerOrReadOnly
from common.pagination import CustomPagination, StandardResultsSetPagination

# Meal
class MealCreateAPIView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    pagination_class = CustomPagination

class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


# MealFood
class MealFoodCreateAPIView(generics.ListCreateAPIView):
    queryset = MealFood.objects.all()
    serializer_class = MealFoodSerializer
    pagination_class = CustomPagination

class MealFoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealFood.objects.all()
    serializer_class = MealFoodSerializer


# HealthMetrics
class HealthMetricsCreateAPIView(generics.ListCreateAPIView):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    pagination_class = CustomPagination

class HealthMetricsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
