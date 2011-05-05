from django.contrib import admin

from contact_form.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'body',)
    
admin.site.register(Contact, ContactAdmin)