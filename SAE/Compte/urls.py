from django.urls import path
from . import views
from django.urls import path
from .views import liste_comptes, creer_compte, detail_compte






urlpatterns = [
    path('liste', views.transaction_list,),
    path('', liste_comptes, name='liste_comptes'),
    path('creer/', creer_compte, name='creer_compte'),
    path('detail/<int:compte_id>/', detail_compte, name='detail_compte'),
]
