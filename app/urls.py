from django.urls import path
from .views import BudgetListView

urlpatterns = [
    path('budgets/', BudgetListView.as_view(), name='Budget_List'),
]
