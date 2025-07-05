from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, UserSerializer
from django.contrib.auth.models import User


from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Expense Tracker API',
        'endpoints': {
            'register': '/api/auth/register/',
            'login': '/api/auth/login/',
            'expenses': '/api/expenses/'
        }
    })

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
