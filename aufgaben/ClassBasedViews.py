import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from .forms import *


def index(request):
    Aufgaben = Aufgabe.objects.all()

    form = AufgabeForm()

    if request.method == 'POST':
        form = AufgabeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'Aufgaben': Aufgaben, 'form': form}
    return render(request, 'Aufgaben/list.html', context)


def updateAufgabe(request, pk):
    aufgabe = Aufgabe.objects.get(id=pk)

    form = AufgabeForm(instance=aufgabe)

    if request.method == 'POST':
        form = AufgabeForm(request.POST, instance=aufgabe)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'Aufgaben/update_aufgabe.html', context)


def deleteAufgabe(request, pk):
    item = Aufgabe.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'Aufgaben/delete.html', context)
