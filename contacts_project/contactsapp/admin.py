from django.contrib import admin
from contactsapp.models import Organization, Contact

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Contact)