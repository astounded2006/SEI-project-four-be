from django.urls import path
from .views import UserRegisterView, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/<int:pk>/', UserProfileView.as_view())
]
