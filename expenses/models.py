from django.db import models
from django.contrib.auth.models import User

class ExpenseIncome(models.Model):
    CREDIT = 'credit'
    DEBIT = 'debit'
    TYPE_CHOICES = [
        (CREDIT, 'Credit'),
        (DEBIT, 'Debit'),
    ]
    
    FLAT = 'flat'
    PERCENT = 'percent'
    TAX_CHOICES = [
        (FLAT, 'Flat'),
        (PERCENT, 'Percentage'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_type = models.CharField(max_length=10, choices=TAX_CHOICES, default=FLAT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def total(self):
        if self.tax_type == self.FLAT:
            return float(self.amount) + float(self.tax)
        else:
            return float(self.amount) + (float(self.amount) * float(self.tax) / 100)
    
    def __str__(self):
        return f"{self.title} - {self.amount}"