from services.models import *
from django.contrib import admin
	
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc', 'pub_date',)
	date_hierarchy = 'pub_date'
	
admin.site.register(Service, ServiceAdmin)