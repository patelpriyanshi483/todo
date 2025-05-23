from django.contrib import admin
from contact.models import Contact
class contactadmin(admin.ModelAdmin):
    list_display=('contact_name','contact_email','contact_number')
admin.site.register(Contact,contactadmin)
# Register your models here.
