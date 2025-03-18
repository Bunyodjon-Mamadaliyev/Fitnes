from django.contrib import admin
from .models import Workout, WorkoutExercise, Food

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'duration')
    list_filter = ('date',)
    search_fields = ('user__username',)

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'sets', 'reps', 'weight')
    list_filter = ('workout', 'exercise')
    search_fields = ('exercise__name',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'carbs', 'fats')
    search_fields = ('name',)
