from django.contrib import admin
from django.apps import apps

#from main.models import models

#ms = apps.get_models(models)

#for model in ms:
#    admin.site.register(model)

from main.models import Orderers
@admin.register(Orderers)
class OrderersAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('familyName',)} 
    list_display=['familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    list_editable=['name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    search_fields=['familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    list_filter=['familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    fields=['familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']

from main.models import UnitsCategories
@admin.register(UnitsCategories)
class UnitsCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','note','slug']
    list_editable=['note','slug']
    search_fields=['name','note','slug']
    list_filter=['name','note','slug']
    fields=['name','note','slug']

from main.models import Units
@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','unitCategory','note','slug']
    list_editable=['unitCategory','note','slug']
    search_fields=['name','unitCategory','note','slug']
    list_filter=['name','unitCategory','note','slug']
    fields=['name','unitCategory','note','slug']

from main.models import Sources
@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','address','route','mapChart','mapSketch','mapDemonstrableForm','photo','description','note','slug']
    list_editable=['address','route','mapChart','mapSketch','mapDemonstrableForm','photo','description','note','slug']
    search_fields=['name','address','route','mapChart','mapSketch','mapDemonstrableForm','photo','description','note','slug']
    list_filter=['name','address','route','mapChart','mapSketch','mapDemonstrableForm','photo','description','note','slug']
    fields=['name','address','route','mapChart','mapSketch','mapDemonstrableForm','photo','description','note','slug']

from main.models import EquipmentsCategories
@admin.register(EquipmentsCategories)
class EquipmentCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','note','slug']
    list_editable=['note','slug']
    search_fields=['name','note','slug']
    list_filter=['name','note','slug']
    fields=['name','note','slug']

from main.models import Equipments
@admin.register(Equipments)
class EquipmentsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','equipmentCategory','source','chart','sketch','photo','demonstrableForm','description','note','slug']
    list_editable=['equipmentCategory','source','chart','sketch','photo','demonstrableForm','description','note','slug']
    search_fields=['name','equipmentCategory','source','chart','sketch','photo','demonstrableForm','description','note','slug']
    list_filter=['name','equipmentCategory','source','chart','sketch','photo','demonstrableForm','description','note','slug']
    fields=['name','equipmentCategory','source','chart','sketch','photo','demonstrableForm','description','note','slug']

from main.models import Amortizations
@admin.register(Amortizations)
class AmortizationsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('equipment',)} 
    list_display=['equipment','note','slug']
    list_editable=['note','slug']
    search_fields=['equipment','note','slug']
    list_filter=['equipment','note','slug']
    fields=['equipment','note','slug']

from main.models import OperationsCategories
@admin.register(OperationsCategories)
class OperationCategorysAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','note','slug']
    list_editable=['note','slug']
    search_fields=['name','note','slug']
    list_filter=['name','note','slug']
    fields=['familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']

from main.models import ComponentsTechCategories
@admin.register(ComponentsTechCategories)
class ComponentsTechCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','parent','note','slug']
    list_editable=['parent','note','slug']
    search_fields=['name','parent','note','slug']
    list_filter=['name','parent','note','slug']
    fields=['name','parent','note','slug']

from main.models import ComponentsProjCategories
@admin.register(ComponentsProjCategories)
class ComponentsProjCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','parent','note','slug']
    list_editable=['parent','note','slug']
    search_fields=['name','parent','note','slug']
    list_filter=['name','parent','note','slug']
    fields=['name','parent','note','slug']

from main.models import ComponentsGoals
@admin.register(ComponentsGoals)
class ComponentsGoalsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','parent','note','slug']
    list_editable=['parent','note','slug']
    search_fields=['name','parent','note','slug']
    list_filter=['name','parent','note','slug']
    fields=['name','parent','note','slug']

from main.models import Components
@admin.register(Components)
class ComponentsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','componentTechCategory','componentProjCategory','componentGoal','quantity','unit','source','chart','sketch','photo','demonstrableForm','description','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    list_editable=['componentTechCategory','componentProjCategory','componentGoal','quantity','unit','source','chart','sketch','photo','demonstrableForm','description','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    search_fields=['name','componentTechCategory','componentProjCategory','componentGoal','quantity','unit','owners','source','chart','sketch','photo','demonstrableForm','description','сomponentsOperations','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    list_filter=['name','componentTechCategory','componentProjCategory','componentGoal','quantity','unit','owners','source','chart','sketch','photo','demonstrableForm','description','сomponentsOperations','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    fields=['name','componentTechCategory','componentProjCategory','componentGoal','quantity','unit','source','chart','sketch','photo','demonstrableForm','description','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']

from main.models import Projects
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    list_editable=['planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    search_fields=['name','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    list_filter=['name','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']
    fields=['name','planTime','startDateTame','finishDateTame','price','discount','selfCost','note','slug']

#from main.models import ProjectsComponents
#@admin.register(ProjectsComponents)
#class ProjectsComponentsAdmin(admin.ModelAdmin):
#    prepopulated_fields={'slug':('component',)} 

from main.models import Operations
@admin.register(Operations)
class OperationsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}  
    list_display=['name','time','unit','cost','category','equipment','multiplier','unitTime','salary','amortization','note','slug']
    list_editable=['time','unit','cost','category','equipment','multiplier','unitTime','salary','amortization','note','slug']
    search_fields=['familyName','name','secondName','enterprise','dateOfBirth','address','telephones','photo','note','slug']
    list_filter=['name','time','unit','cost','category','equipment','multiplier','unitTime','salary','amortization','note','slug']
    fields=['name','time','unit','cost','category','equipment','multiplier','unitTime','salary','amortization','note','slug']

#from main.models import ComponentsOperations
#@admin.register(ComponentsOperations)
#class ComponentsOperationsAdmin(admin.ModelAdmin):
#    prepopulated_fields={'slug':('component',)}  

from main.models import OperationsStatuses
@admin.register(OperationsStatuses)
class OperationStatusesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
    list_display=['name','note','slug']
    list_editable=['note','slug']
    search_fields=['name','note','slug']
    list_filter=['name','note','slug']
    fields=['name','note','slug']

#from main.models import ProjectsOperations
#@admin.register(ProjectsOperations)
#class ProjectsOperationsAdmin(admin.ModelAdmin):
#    prepopulated_fields={'slug':('project',)}

from main.models import Orders
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('dateTime',)} 
    list_display=['id','dateTime','orderer','project','note','slug']
    list_editable=['dateTime','orderer','project','note','slug']
    search_fields=['dateTime','orderer','project','note','slug']
    list_filter=['dateTime','orderer','project','note','slug']
    fields=['dateTime','orderer','project','note','slug']

from main.models import Workers
@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('familyName',)}  
    list_display=['familyName','name','secondName','passport','dateOfBirth','address','telephones','photo','note','slug']
    list_editable=['name','secondName','passport','dateOfBirth','address','telephones','photo','note','slug']
    search_fields=['familyName','name','secondName','passport','dateOfBirth','address','telephones','photo','note','slug']
    list_filter=['familyName','name','secondName','passport','dateOfBirth','address','telephones','photo','note','slug']
    fields=['familyName','name','secondName','passport','dateOfBirth','address','telephones','photo','note','slug']

from main.models import Works
@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('project',)} 
    list_display=['startDateTimeOperation','finishtDateTimeOperation','workTime','worker','project','operation','makeWork','note','slug']
    list_editable=['finishtDateTimeOperation','workTime','worker','project','operation','makeWork','note','slug']
    search_fields=['startDateTimeOperation','finishtDateTimeOperation','workTime','worker','project','operation','makeWork','note','slug']
    list_filter=['startDateTimeOperation','finishtDateTimeOperation','workTime','worker','project','operation','makeWork','note','slug']
    fields=['startDateTimeOperation','finishtDateTimeOperation','workTime','worker','project','operation','makeWork','note','slug']

from main.models import Storage
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('dateTime',)}   
    list_display=['dateTime','component','quantity','note','slug']
    list_editable=['component','quantity','note','slug']
    search_fields=['dateTime','component','quantity','note','slug']
    list_filter=['dateTime','component','quantity','note','slug']
    fields=['dateTime','component','quantity','note','slug']
