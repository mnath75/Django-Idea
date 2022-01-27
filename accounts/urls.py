from django.urls import path, include
from django.urls.conf import re_path
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from django.views.generic import TemplateView

urlpatterns = [
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset/confirm/<uidb64>/<token>/', TemplateView.as_view(), name='password_reset_confirm'), #dummy view
]
