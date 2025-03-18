from rest_framework import serializers
from .models import Workout, WorkoutExercise, Food
from users.serializers import ExerciseSerializer

# Workout
class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'user', 'date', 'duration', 'exercises']
        read_only_fields = ['id']

# WorkoutExercise
class WorkoutExerciseSerializer(serializers.ModelSerializer):
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    class Meta:
        model = WorkoutExercise
        fields = ['id', 'workout', 'exercise', 'sets', 'reps', 'weight']
        read_only_fields = ['id']

# Food
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'protein', 'carbs', 'fats']
        read_only_fields = ['id']

