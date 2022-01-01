from django.urls import path
from core import views

urlpatterns = [
    path('verificationmail/', views.send_verification_mail.as_view()),
    path('sendpassmail/', views.send_pass_change_email.as_view())
]   