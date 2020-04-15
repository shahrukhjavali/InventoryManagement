from django.urls import path
from.views import UomListView,AddUom

urlpatterns = [
    path('viewuom',UomListView.as_view(),name='uomview'),
    path('adduom',AddUom.as_view(),name='adduom'),

]