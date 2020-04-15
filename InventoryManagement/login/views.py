from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from .models import UserRole

class LoginView(View):
    
    def get(self,request):
        return render(self.request,'registration/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            userrole = UserRole.objects.get(user=user)
            #messages.success(request,"User logged in successfully!")
            self.request.session['is_loggedin'] = True
            login(self.request,user)
            return render(self.request,'login/home.html',{'userole':userrole})
        else:
            messages.error(request,"Username or password is invalid, please try again!")
            return render(self.request,'registration/login.html')

class LogoutView(View):

    def get(self,request):
        del self.request.session['is_loggedin']
        logout(self.request)
        return HttpResponseRedirect('/accounts/login')

class HomeView(View):
    
    def get(self,request):
        if self.request.session['is_loggedin']:
            userrole = UserRole.objects.get(user=request.user)
            return render(self.request,'login/home.html',{'userole':userrole})
        else:
            return HttpResponseRedirect('/accounts/login')


