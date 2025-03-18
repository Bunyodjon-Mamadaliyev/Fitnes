from rest_framework import generics, permissions
from .models import Workout, WorkoutExercise, Food
from .serializers import WorkoutSerializer, WorkoutExerciseSerializer, FoodSerializer
from common.permissions import IsOwnerOrReadOnly
from common.pagination import CustomPagination

# Workout
class WorkoutCreateAPIView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    pagination_class = CustomPagination

class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# WorkoutExercise
class WorkoutExerciseCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer
    pagination_class = CustomPagination

class WorkoutExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer

# Food
class FoodCreateAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = CustomPagination

class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
