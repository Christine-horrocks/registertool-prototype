from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PickCsvForm, DeveloperAgreementTransactionForm, DeveloperAgreementContributionForm, DeveloperAgreementForm
from .forms import dynamic_form
import csv

def pick_csv(request):

    if request.method == 'POST':
        form = PickCsvForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            request.session['category'] = category
            return HttpResponseRedirect('add_entry')

    form = PickCsvForm()
    return render(request, 'dev_con/form.html', {'form': form})




def add_entry(request):

    category = request.session.get('category')
    if request.method == 'POST':
        form = formpicker(category, request)
        if form.is_valid():
            data = form.cleaned_data
            update_developer_agreement_csv(category, data)
            return HttpResponseRedirect('entry_complete')


    # form = formpicker(category, request)
    form = dynamic_form()
    return render(request, 'dev_con/add_entry_form.html', {'form': form})









def entry_complete(request):
    category = request.session.get('category')
    with open(f'{category}.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reversed(list(csv_reader)):
            data.append(', '.join(row))

    return render(request, 'dev_con/entry_complete.html', {'data': data[0]})


def formpicker(choice, request):

    return {
        'developer-agreement-contributions': DeveloperAgreementContributionForm(request.POST),
        'developer-agreements': DeveloperAgreementForm(request.POST),
        'developer-agreement-transactions': DeveloperAgreementTransactionForm(request.POST)
    }[choice]


def update_developer_agreement_csv(choice, data):
    data_array = list(data.values())
    print(data_array)
    with open(f'{choice}.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(data_array)
