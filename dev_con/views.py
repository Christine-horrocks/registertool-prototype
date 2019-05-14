from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def pick_csv(request):
    return render(request, 'dev_con/base.html')
