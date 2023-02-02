# app.py
from django.db import models

class Loan(models.Model):
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    loan_term = models.IntegerField()
    loan_date = models.DateField(auto_now_add=True)

# views.py
from django.shortcuts import render
from .models import Loan

def loan_application(request):
    if request.method == 'POST':
        loan_amount = request.POST['loan_amount']
        interest_rate = request.POST['interest_rate']
        loan_term = request.POST['loan_term']
        Loan.objects.create(loan_amount=loan_amount, interest_rate=interest_rate, loan_term=loan_term)
        return render(request, 'loan_application_success.html')
    return render(request, 'loan_application.html')

# urls.py
from django.urls import path
from .views import loan_application

urlpatterns = [
    path('loan_application/', loan_application, name='loan_application'),
]
