from django.urls import path
from .views import InvListView,ViewAddInventory

urlpatterns = [
    path('viewinventory',InvListView.as_view(),name='invview'),
    path('addinv/<int:id>',ViewAddInventory.as_view(),name='addinv'),
]