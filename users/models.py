from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# User
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    def __str__(self):
        return self.username

# UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ACTIVITY_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly Active'),
        ('moderately_active', 'Moderately Active'),
        ('very_active', 'Very Active'),
        ('extra_active', 'Extra Active'),
    ]
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    GOAL_CHOICES = [
        ('lose_weight', 'Lose Weight'),
        ('maintain_weight', 'Maintain Weight'),
        ('gain_weight', 'Gain Weight'),
        ('build_muscle', 'Build Muscle'),
    ]
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)




# Exercise
class Exercise(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ]
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    calories_burned_per_hour = models.PositiveIntegerField()

    def __str__(self):
        return self.name