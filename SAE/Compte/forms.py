from django import forms
from .models import Transaction
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from django import forms
from .models import Compte

class CompteForm(forms.ModelForm):
    class Meta:
        model = Compte
        fields = ['nom']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account_number', 'amount']