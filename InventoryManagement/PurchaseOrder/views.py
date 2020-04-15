from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,View
from .models import PurchaserOrder,PoItems
import random
from supplier.models import Supplier
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from master.models import Uom
from product.models import Product
from login.models import UserRole

class POListView(View):

    def get(self,request):
        pos = PurchaserOrder.objects.all()
        user = UserRole.objects.get(user=request.user)
        print(user.role)
        return render(self.request,'po/viewpo.html',{'pos':pos,'user':user})
    
class PoDetailedView(View):

    def get(self,request,*args,**kwagrs):
        po = PurchaserOrder.objects.get(id=kwagrs['id'])
        podetailed = PoItems.objects.filter(po_id=kwagrs['id'])
        return render(self.request,'po/podetailed.html',{'podetailed':podetailed,'po':po})
    
class AddPurchaseOrder(View):
     po = PurchaserOrder()
     pr_number=random.randint(0,999999999999)
     order_date = timezone.now()
     def get(self,request):
         suppliers = Supplier.objects.all()
         return render(self.request,'po/addpo.html',{'addpoobj':AddPurchaseOrder,'suppliers':suppliers})

     def post(self,request):
         self.po.prnumber = self.pr_number
         self.po.orderdate = self.order_date
         self.po.orderedby = self.request.user
         self.po.supplier = Supplier.objects.get(id=request.POST.get('selsupplier'))
         self.po.status = True
         self.po.tax = request.POST.get('tax')
         self.po.Approval = 'Created'
         self.po.Approval_comments = request.POST.get('comment')
         self.po.save()
         print(self.po.id)
         return HttpResponseRedirect('/po/additemspo/'+str(self.po.id))

class Additemstopo(View):

    def get(self,request,*args,**kwargs):
        #poobj = PurchaserOrder.objects.get(id=kwargs['id'])
        products = Product.objects.filter(status=True)
        uoms = Uom.objects.filter(status=True)
        return render(self.request,'po/addpo2.html',{'products':products,'uoms':uoms})

    def post(self,request,*args,**kwargs):
        addpoitems = PoItems.objects.filter(po = PurchaserOrder.objects.get(id=kwargs['id']),
            products=Product.objects.get(id=request.POST.get('product')),
        ).first()
        if addpoitems is not None:
            addpoitems.quantity = int(addpoitems.quantity)+int(request.POST.get('qty'))    
            addpoitems.total = int(addpoitems.total) + int(Product.objects.get(id=request.POST.get('product')).price)*int(request.POST.get('qty'))     
            addpoitems.product_status = True
            addpoitems.last_update_by = request.user
            addpoitems.last_update_date = timezone.now()
            addpoitems.save()
        else:
            tax = int(PurchaserOrder.objects.get(id=kwargs['id']).tax)
            p = int(Product.objects.get(id=request.POST.get('product')).price)
            taxamt = (tax*p)/100
            PoItems.objects.create(
                products = Product.objects.get(id=request.POST.get('product')),
                po = PurchaserOrder.objects.get(id=kwargs['id']),
                quantity = int(request.POST.get('qty')),
                uom = Uom.objects.get(id=request.POST.get('uom')),
                total = taxamt+int(Product.objects.get(id=request.POST.get('product')).price)*int(request.POST.get('qty')),
                product_status = True,
                last_update_by = request.user,
                last_update_date = timezone.now(), 
            )
        return HttpResponseRedirect('/po/additemspo/'+str(kwargs['id']))


class IncludePoview(View):
    
    def post(self,request,*args,**kwargs):
        poitem = PoItems.objects.get(id=kwargs['id'])
        print(poitem)
        if poitem.product_status is True:
            poitem.product_status = False
            poitem.last_update_by = request.user
            poitem.last_update_date = timezone.now()
            poitem.save()
        else:
            poitem.product_status = True
            poitem.last_update_by = request.user
            poitem.last_update_date = timezone.now()
            poitem.save()
        return HttpResponseRedirect('/po/podetailed/5')

class ApprovalView(View):

    def get(self,request,*args,**kwargs):
        obj = PurchaserOrder.objects.get(id=kwargs['id'])
        return render(self.request,'po/approval.html',{'obj':obj})

    def post(self,request,*args,**kwargs):
        poobj = PurchaserOrder.objects.get(prnumber=request.POST.get('ponum'))
        poobj.Approval = request.POST.get('selcomment')
        poobj.Approval_comments = request.POST.get('comments')
        poobj.save()
        return HttpResponseRedirect('/po/viewpo')

