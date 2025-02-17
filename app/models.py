from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tags = models.JSONField(blank=True, null=True)  # Stores list of tags as JSON
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"


class Budget(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField(default=now)  # Stores the month-year of the budget
    created_at = models.DateTimeField(auto_now_add=True)

    def remaining_amount(self):
        from django.db.models import Sum
        total_expense = self.user.expenses.filter(category=self.category, date__month=self.month.month, date__year=self.month.year).aggregate(Sum('amount'))['amount__sum'] or 0
        return self.budget_limit - total_expense

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.budget_limit}"
