from django.urls import path
from .views import (SignupView, LoginView, LogoutView,  UserProfileView, UserProfileDetailView,
                    ExerciseListCreateView, ExerciseDetailView
                    )
urlpatterns = [
    path("auth/signup/", SignupView.as_view(), name="signup"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path('users/profile/', UserProfileView.as_view(), name='user-profile'),
    path('users/profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path("exercises/", ExerciseListCreateView.as_view(), name="exercise-list"),
    path("exercises/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
]
