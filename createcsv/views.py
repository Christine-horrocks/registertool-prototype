from django.shortcuts import render
from django.shortcuts import redirect, render_to_response
from .forms import CreateCsvForm
from .forms import UpdateCsvForm
import csv
from django.http import HttpResponseRedirect

def homepage(request):

    if request.method == 'POST':
        form = CreateCsvForm(request.POST)
        if form.is_valid():
            register = form.cleaned_data['register']
            headers = form.cleaned_data['headers']
            headersarray = headers.split(',')
            create_csv(register, headersarray)

    form = CreateCsvForm()
    return render(request, 'form.html', {'form': form})


def updatepage(request):
    extra_headings = ['first_name_schema', 'last_name_schema', 'head']
    form = UpdateCsvForm(request.POST or None, extra=extra_headings)
    if form.is_valid():
        # for (heading, input) in form.headings_input():
        #     save_input(request, heading, answer)
        # register = form.cleaned_data['register']
        print(form)
        return HttpResponseRedirect('/')

    return render(request, 'form.html', {'form': form})


def addinfopage(request):
    return render(request, 'createcsv/home.html')


def create_csv(filename, column_headers):
    with open(f'{filename}.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(column_headers)
        print(f'The file {filename}.csv has been created')

#
# def append_to_csv(self, filename, entry_data):
#     with open(f'{filename}.csv', 'a') as csvfile:
#         filewriter = csv.writer(csvfile)
#         filewriter.writerow(entry_data)