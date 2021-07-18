from django.shortcuts import render
from .models import TblAccount, TblIncome

# Create your views here.

def index(request):
    test = TblAccount.objects.all()
    print(test)
    return render(request, 'incomeapp/index.html')