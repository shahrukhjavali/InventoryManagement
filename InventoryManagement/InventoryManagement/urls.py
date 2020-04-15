from django.contrib import admin
from django.urls import path,include
from login.views import HomeView,LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',LoginView.as_view(),name='login'),
    path('',HomeView.as_view(),name='home'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('master/',include('master.urls')),
    path('po/',include('PurchaseOrder.urls')),
    path('supplier/',include('supplier.urls')),
    path('inventory/',include('inventory.urls')),
]
