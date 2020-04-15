from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Inventory
from product.models import Product
from django.utils import timezone
from PurchaseOrder.models import PurchaserOrder,PoItems
from django.http import HttpResponseRedirect

class InvListView(ListView):
    model = Inventory
    context_object_name = 'inv'
    template_name = 'inv/viewinv.html'

class ViewAddInventory(View):

    def post(self,request,*args,**kwargs):
        POS = PurchaserOrder.objects.get(Approval='Received',id=kwargs['id'])
        listofitms = PoItems.objects.filter(po_id=POS.id,product_status=True)
        for item in listofitms:
            invitm = Inventory.objects.filter(items=item.products).first()
            if invitm is not None:
                invitm.qty = invitm.qty+item.quantity
                invitm.createdby = request.user
                invitm.creation_date = timezone.now()
                invitm.last_update_by = request.user
                invitm.last_update_date = timezone.now()
                invitm.save()
                POS.Approval = 'Updated Inventory'
                POS.save()
            else:
                Inventory.objects.create(
                    items = item.products,
                    qty = item.quantity,
                    createdby = request.user,
                    creation_date = timezone.now(),
                    last_update_by = request.user,
                    last_update_date = timezone.now(),
                )   
                POS.Approval = 'Created Inventory'
                POS.save()
        return HttpResponseRedirect('/inventory/viewinventory')

    

