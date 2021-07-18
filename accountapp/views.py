from django.shortcuts import render
from incomeapp.models import TblAccount, TblIncome

# Create your views here.

def login(request):
    income = TblIncome.objects.all()
    print(income)
    return render(request,'accountapp/login.html')