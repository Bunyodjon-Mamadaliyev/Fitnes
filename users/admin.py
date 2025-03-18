from django.contrib import admin
from .models import User, UserProfile, Exercise

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'gender')
    list_filter = ('gender',)
    search_fields = ('username', 'email')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'activity_level', 'goal')
    list_filter = ('activity_level', 'goal')
    search_fields = ('user__username',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'calories_burned_per_hour')
    list_filter = ('category',)
    search_fields = ('name',)
