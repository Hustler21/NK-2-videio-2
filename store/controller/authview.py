from django.shortcuts import redirect, render

from django.contrib import messages

def register(request):
    return render(request,"store/register.html")