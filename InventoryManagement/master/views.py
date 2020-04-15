from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Uom
from django.http import HttpResponseRedirect
from django.utils import timezone
from login.models import UserRole

class UomListView(ListView):
    model = Uom
    context_object_name = 'uoms'
    template_name = 'master/viewuom.html'

class AddUom(View):

    def get(self,request):
        return render(self.request,'master/adduom.html')
    
    def post(self,request):
        uom = Uom()
        uom.name = request.POST.get('uomname')
        uom.desc = request.POST.get('uomdesc')
        uom.status = True
        uom.createdby = request.user
        uom.created_date = timezone.now()
        uom.last_update_by = request.user
        uom.last_update_date = timezone.now()
        uom.save()
        return HttpResponseRedirect('/master/viewuom')