from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,validators
from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
@requires_csrf_token
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
        else:
            messages.error(request, "Error")
    else:
        form=RegisterForm()
    
    
    return render(request,"registration/register.html",{"form":form})