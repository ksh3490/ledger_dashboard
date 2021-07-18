from django.shortcuts import render
from .models import TblAccount, TblIncome

# Create your views here.

def index(request):
    return render(request, 'incomeapp/index.html')