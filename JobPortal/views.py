from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect
from .models import jobopenings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import admin

@login_required
def home(request):
    print ("Test")
    if request.user.is_superuser:
        print("Super")
        return HttpResponseRedirect("http://127.0.0.1:8000/admin/")
    else:
        total_opening=list(jobopenings.objects.get_queryset())
        return render(request,"JobPortal/home.html",
                  {'nopenings':total_opening})
    return render(request, "JobPortal/home.html")



def logout_view(request):
    logout(request)
    return redirect('home')