from django.urls import path
from .views import (WorkoutCreateAPIView, WorkoutDetailView,
                    WorkoutExerciseCreateAPIView, WorkoutExerciseDetailView,
                    FoodCreateAPIView, FoodDetailView
                    )
urlpatterns = [
    path('workout/', WorkoutCreateAPIView.as_view(), name='workout-list-create'),
    path('workout/<int:pk>/', WorkoutDetailView.as_view(), name='workout-list'),
    path('workoutExercise/', WorkoutExerciseCreateAPIView.as_view(), name='workoutExercise-list-create'),
    path('workoutExercise/<int:pk>/', WorkoutExerciseDetailView.as_view(), name='workoutExercise-list'),
    path('food/', FoodCreateAPIView.as_view(), name='food-list-create'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='food-list'),
]


