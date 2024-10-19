from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User

#from main.models import models

#ms = apps.get_models(models)

#for model in ms:
#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('familyName',)} 
    list_display=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    list_editable=['first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    search_fields=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    list_filter=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    fields=['username','first_name','last_name','email','image','familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']

    inlines=[CartTabAdmin,OrderTabulareAdmin]

#from main.models import Orderers
#@admin.register(Orderers)
#class OrderersAdmin(admin.ModelAdmin):
#    prepopulated_fields={'slug':('familyName',)} 

