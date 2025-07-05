from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from expenses.views import UserCreateView
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='/api/expenses/')),  # Add this line
  
    path('admin/', admin.site.urls),
    path('api/auth/register/', UserCreateView.as_view({'post': 'create'}), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/expenses/', include('expenses.urls')),
]