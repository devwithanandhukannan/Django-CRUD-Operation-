from django.urls import path
from .views import UserRegister, UserLogin, Logout, ProfileView

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', Logout.as_view()),
    path('profile/', ProfileView.as_view()),
]
