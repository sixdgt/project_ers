from django.urls import path
from .views import LoginVew, RegisterView

urlpatterns = [
    path('login/', LoginVew.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]