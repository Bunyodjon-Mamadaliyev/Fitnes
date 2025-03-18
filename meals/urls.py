from django.urls import path
from .views import (MealCreateAPIView, MealDetailView,
                    MealFoodCreateAPIView, MealFoodDetailView,
                    HealthMetricsCreateAPIView, HealthMetricsDetailView
                    )
urlpatterns = [
    path('meals/', MealCreateAPIView.as_view(), name='meal-list-create'),
    path('meals/<int:pk>/', MealDetailView.as_view(), name='meal-list'),
    path('meal-food/', MealFoodCreateAPIView.as_view(), name='meal-list'),
    path('meal-food/<int:pk>/', MealFoodDetailView.as_view(), name='meal-list'),
    path('health-metrics/', HealthMetricsCreateAPIView.as_view(), name='health-metrics-list-create'),
    path('health-metrics/<int:pk>/', HealthMetricsDetailView.as_view(), name='health-metrics-list'),
]

