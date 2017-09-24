
from django.shortcuts import render
from .models import Contacts
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class ContactCreate(CreateView):

    model = Contacts
    fields = ('name', 'contact_number', 'email', 'business', 'enquiry')

    success_url = reverse_lazy('home')

