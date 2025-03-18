from rest_framework import serializers
from .models import Meal, MealFood, HealthMetrics

# Meal
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'user', 'date', 'meal_type', 'foods']
        read_only_fields = ['id']

# MealFood
class MealFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealFood
        fields = ['id', 'meal', 'food', 'quantity']
        read_only_fields = ['id']

# HealthMetrics
class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = ['id', 'user', 'date', 'weight', 'body_fat_percentage', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate']
        read_only_fields = ['id']
