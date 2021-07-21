from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth.models import User

from incomeapp.models import TblIncome

from django.db.models import Sum
from django.db.models import Q

# Create your views here.

def index(request):
    income_items = TblIncome.objects.filter(user = request.user).order_by('-income_dt')

    total_income = TblIncome.objects.filter(user=request.user).aggregate(total_income=Sum('income_value',filter=Q(income_value__gt=0)))

    return render(request, 'incomeapp/index.html', context={
        'user': request.user,
        'income_items': income_items,
        'total_income': total_income['total_income'],
    })

def add_item(request):
    name = request.POST['income_name']
    value = request.POST['income_value']
    date = request.POST['income_dt']

    item = TblIncome.objects
    item.create(income_name = name, income_value = value, income_dt = date, user=request.user)

    total_income = TblIncome.objects.filter(user=request.user).aggregate(total_income=Sum('income_value',filter=Q(income_value__gt=0)))

    return HttpResponseRedirect('/income/')

def delete_item(request, income_item_id):
    item = TblIncome.objects.get(id=income_item_id)
    item.delete()

    return HttpResponseRedirect('/income/')