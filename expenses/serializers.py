from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = ExpenseIncome
        fields = ['id', 'user', 'title', 'description', 'amount', 
                 'transaction_type', 'tax', 'tax_type', 'total',
                 'created_at', 'updated_at']
        read_only_fields = ['user', 'total', 'created_at', 'updated_at']
    
    def get_total(self, obj):
        return obj.total