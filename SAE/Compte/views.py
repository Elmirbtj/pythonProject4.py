import asyncio

from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.shortcuts import render, redirect
from .forms import CompteForm
from .models import Compte
from django.shortcuts import render, get_object_or_404
from .models import Compte

from decimal import Decimal

from django.http import HttpResponse
from nats.aio.client import Client as NATS



def detail_compte(request, compte_id):
    compte = Compte.objects.get(id=compte_id)
    if request.method == 'POST':
        montant = Decimal(request.POST.get('montant'))  # Convertir le montant en Decimal
        compte.montant_actuel += montant
        compte.save()
    return render(request, 'detail_compte.html', {'compte': compte})
def liste_comptes(request):
    comptes = Compte.objects.all()
    return render(request, 'liste_comptes.html', {'comptes': comptes})

def creer_compte(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        Compte.objects.create(nom=nom)
        return redirect('liste_comptes')
    return render(request, 'creer_compte.html')


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})
