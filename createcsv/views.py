from django.shortcuts import render
from django.shortcuts import redirect, render_to_response
from .forms import LocalPlansForm
from .forms import PickModel
import csv
from django.http import HttpResponseRedirect

def homepage(request):

    if request.method == 'POST':
        form = PickModel(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            print(category)
            return HttpResponseRedirect('updateform')

    form = PickModel()
    return render(request, 'form.html', {'form': form})

def updateform(request):

    if request.method == 'POST':
        form = LocalPlansForm(request.POST)
        if form.is_valid():
            new_line = form.save()
            return HttpResponseRedirect('uploadcomplete')

    form = LocalPlansForm()
    return render(request, 'form.html', {'form': form})


def uploadcomplete(request):

    return render(request, 'createcsv/home.html')


#
#
# def create_csv(filename, column_headers):
#     with open(f'{filename}.csv', 'w') as csvfile:
#         filewriter = csv.writer(csvfile)
#         filewriter.writerow(column_headers)
#         print(f'The file {filename}.csv has been created')

#
# def append_to_csv(self, filename, entry_data):
#     with open(f'{filename}.csv', 'a') as csvfile:
#         filewriter = csv.writer(csvfile)
#         filewriter.writerow(entry_data)