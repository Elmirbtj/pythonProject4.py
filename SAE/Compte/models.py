from django.db import models

class Transaction(models.Model):
    account_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.amount} € (Compte: {self.account_number})"

from django.db import models

class Compte(models.Model):
    nom = models.CharField(max_length=100)
    montant_actuel = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.id} - {self.nom}"
