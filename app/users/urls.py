from django.urls import path
from users.views import RegisterView, UserPersonalDetailsView, UserDeliveryDetailsView, ForgotPasswordView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import TestEmailView
from .views import ActivateUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('personal-details/', UserPersonalDetailsView.as_view(), name='personal_details'),
    path('delivery-details/', UserDeliveryDetailsView.as_view(), name='delivery_details'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('test-email/', TestEmailView.as_view(), name='test-email'),
    path('api/users/activate/<uuid:code>/', ActivateUserView.as_view(), name='user-activate'),
]



