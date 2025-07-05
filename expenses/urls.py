from django.urls import path
from .views import ExpenseIncomeViewSet
from rest_framework.routers import DefaultRouter  # Changed from SimpleRouter

router = DefaultRouter()  # Use DefaultRouter instead
router.register('expenses', ExpenseIncomeViewSet, basename='expenses')  # Added URL prefix

urlpatterns = router.urls