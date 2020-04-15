from django.urls import path
from .views import AddSupplierView,SupplierView

urlpatterns = [
    path('addsupplier',AddSupplierView.as_view(),name='addsupllier'),
    path('supplierview',SupplierView.as_view(),name='supplierview'),
]