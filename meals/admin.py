from django.contrib import admin
from .models import Meal, MealFood, HealthMetrics

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meal_type')
    list_filter = ('meal_type', 'date')
    search_fields = ('user__username', 'meal_type')

@admin.register(MealFood)
class MealFoodAdmin(admin.ModelAdmin):
    list_display = ('meal', 'food', 'quantity')
    list_filter = ('meal',)
    search_fields = ('food__name',)

@admin.register(HealthMetrics)
class HealthMetricsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'weight', 'body_fat_percentage', 'heart_rate')
    list_filter = ('date',)
    search_fields = ('user__username',)

