"""Jumga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from api import views as api_views

urlpatterns = [
    path('cardpayment', api_views.card_payments),
    path('verifypayment', api_views.verify_payment),
    path('validatepayment', api_views.validate_payments),
    path('bankpayment', api_views.ng_bank_payment),
    path('getcsrf', api_views.get_csrf),
    path('auth/', include('accounts.urls')),
]
