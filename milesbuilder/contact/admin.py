
from django.contrib import admin
from .models import Contacts
# Register your models here.


class ContactAdmin(admin.ModelAdmin):

    search_fields = ['name', 'business']

    list_filter = ['business']

    list_display = ['name', 'contact_number', 'email', 'business', 'date', 'enquiry']


admin.site.register(Contacts, ContactAdmin)
