from django.urls import path
from  login.views import LoginView, SendOTPView, VerifyOTPView, ResetPasswordView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('send-otp/', SendOTPView.as_view()),
    path('verify-otp/', VerifyOTPView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
]
