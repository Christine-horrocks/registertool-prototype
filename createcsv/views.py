from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LocalPlansForm, DeveloperContribuationsForm
from .forms import PickModel

def homepage(request):

    if request.method == 'POST':
        form = PickModel(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            request.session['category'] = category
            print(category)
            return HttpResponseRedirect('updateform')

    form = PickModel()
    return render(request, 'createcsv/form.html', {'form': form})

def updateform(request):

    category = request.session.get('category')
    if request.method == 'POST':
        form = formpicker(category, request)
        if form.is_valid():
            new_line = form.save()
            return HttpResponseRedirect('uploadcomplete')


    form = formpicker(category, request)
    return render(request, 'createcsv/update_form.html', {'form': form})


def uploadcomplete(request):

    return render(request, 'createcsv/home.html')


def formpicker(choice, request):

    return {
        'localplans': LocalPlansForm(request.POST),
        'developercontributions': DeveloperContribuationsForm(request.POST),
        'stuffwithtrees': LocalPlansForm(request.POST)
    }[choice]