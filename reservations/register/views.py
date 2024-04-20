from .forms import RegisterForm

from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
@requires_csrf_token
def register(response):
    if response.method=="POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form=RegisterForm()
    
    return render(response,"registration/register.html",{"form":form})