from django.urls import path
from .views import POListView,AddPurchaseOrder,Additemstopo,PoDetailedView,IncludePoview,ApprovalView

urlpatterns = [
    path('viewpo',POListView.as_view(),name='viewpo'),
    path('addpo',AddPurchaseOrder.as_view(),name='addpo'),
    path('additemspo/<int:id>',Additemstopo.as_view(),name='additemstopo'),
    path('podetailed/<int:id>',PoDetailedView.as_view(),name='podetailedview'),
    path('productinclude/<int:id>',IncludePoview.as_view(),name='productinclude'),
    path('approval/<int:id>',ApprovalView.as_view(),name='approval'),
]