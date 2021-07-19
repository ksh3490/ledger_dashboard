from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('income/')
        
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            # return render(request, 'accountapp/sign_up.html', {
            #     'form': form,
            # })
    
    else:
        form = UserCreationForm
        return render(request, 'accountapp/sign_up.html', {
            'form': form,
        })