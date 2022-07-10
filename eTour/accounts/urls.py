from django.urls import path
from .views import CreateUserAPIView,RequestPasswordReset,CurrentUserView
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('check/', CurrentUserView.as_view()),
    path('password-reset/', RequestPasswordReset.as_view(), name = 'request-reset-email'),
]