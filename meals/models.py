from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Meal
class Meal(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField()
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    meal_type = models.CharField(max_length=15, choices=MEAL_CHOICES)
    foods = models.ManyToManyField('workouts.Food', through='MealFood')

    def __str__(self):
        return self.user.username


# MealFood
class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey('workouts.Food', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)



# HealthMetrics
class HealthMetrics(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blood_pressure_systolic = models.PositiveIntegerField(null=True, blank=True)
    blood_pressure_diastolic = models.PositiveIntegerField(null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return f"{self.user} - {self.date}"
