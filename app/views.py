from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Budget
from.serializers import BudgetListSerializer

# Create your views here.

class BudgetListView(ListAPIView):
    model=Budget
    queryset=Budget.objects.all()
    serializer_class=BudgetListSerializer