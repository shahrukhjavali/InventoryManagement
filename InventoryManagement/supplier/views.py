from django.shortcuts import render
from django.views.generic import ListView,View
from login.models import UserRole
from .models import Supplier
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class AddSupplierView(View):

    def get(self,request):
        users =  UserRole.objects.filter(role='Sup')
        return render(self.request,'supplier/addsupplier.html',{'users':users})

    def post(self,request):
        supp = Supplier()
        print(request.POST.get('selsupplier'))
        supp.supplier = UserRole.objects.get(user_id=request.POST.get('selsupplier'))
        supp.mobnum = request.POST.get('mobnum')
        supp.Adderss = request.POST.get('add1')+request.POST.get('add2')
        supp.city = request.POST.get('city')
        supp.state = request.POST.get('state')
        supp.pincode = request.POST.get('pincode')
        supp.email = request.POST.get('email')
        supp.status =  True
        supp.createdby = request.user
        supp.creation_date = timezone.now()
        supp.last_update_by = request.user
        supp.last_update_date = timezone.now()
        supp.save()
        return HttpResponseRedirect('/supplier/supplierview')

class SupplierView(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'supplier/viewsupplier.html'
