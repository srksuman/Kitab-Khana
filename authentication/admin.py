from django.contrib import admin
from .models import PreRegistration
admin.site.site_header = "किताब खाना"
admin.site.site_title = 'किताब खाना'
admin.site.index_title ="किताब खाना"
# Register your models here.

@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = ['username','first_name']
