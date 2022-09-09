from django.urls import path
from . import views

urlpatterns = [
    path('expense/', views.submit_expense, name='submit_expense'),
    path('income/', views.submit_income, name='submit_income'),
]
