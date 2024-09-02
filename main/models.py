from django.db import models
from django.urls import reverse

class UnitsCategories(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #Units=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='UnitCategory'
        verbose_name='Категория единицы'
        verbose_name_plural='Категории единиц'

    def __str__(self) -> str:
        return self.name   

class Units(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True)
    unitCategory=models.ForeignKey(to=UnitsCategories,null=True, verbose_name='Категория единицы', on_delete=models.CASCADE)
    #Operations=models.PositiveIntegerField()
    #RowMaterials=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Unit'
        verbose_name='Единица'
        verbose_name_plural='Единицы'

    def __str__(self) -> str:
        return self.name   

class Sources(models.Model):#источники сырья и комплектующих    
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    address=models.CharField(max_length=150,blank=True,null=True) 
    route=models.CharField(max_length=150,blank=True,null=True)
    mapChart=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Чертёж')
    mapSketch=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Эскиз')
    mapDemonstrableForm=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Наглядное отображение')
    photo=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Фото')
    description=models.TextField(max_length=200,blank=True,null=True,verbose_name='Описание')
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Sources'
        verbose_name='Предприятие'
        verbose_name_plural='Предприятия'

    def __str__(self) -> str:
        return self.name   

class Orderers(models.Model):
    familyName=models.CharField(max_length=150,blank=True,null=True,verbose_name='Фамилия')
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Имя')
    secondName=models.CharField(max_length=150,blank=True,null=True,verbose_name='Отчество')
    enterprise=models.ForeignKey(to=Sources,null=True, verbose_name='Предприятие', on_delete=models.CASCADE)
    dateOfBirth=models.DateTimeField(blank=True,null=True,verbose_name='Дата рождения')
    address=models.CharField(max_length=150,blank=True,null=True) 
    telephones=models.CharField(max_length=150,blank=True,null=True) 
    photo=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Фото')
    #Orders=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Orderer'
        verbose_name='Заказчик'
        verbose_name_plural='Заказчики'

    def __str__(self) -> str:
        return self.familyName   

class EquipmentsCategories(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='EquipmentCategory'
        verbose_name='Категория оборудования'
        verbose_name_plural='Категории оборудования'

    def __str__(self) -> str:
        return self.name   

class Equipments(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    equipmentCategory=models.ForeignKey(to=EquipmentsCategories,null=True, verbose_name='Категория проекта', on_delete=models.CASCADE)
    source=models.ForeignKey(to=Sources,null=True, verbose_name='Источник', on_delete=models.CASCADE)
    chart=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Чертёж')
    sketch=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Эскиз')
    photo=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Фото')
    demonstrableForm=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Наглядное отображение')
    description=models.TextField(max_length=200,blank=True,null=True,verbose_name='Описание')
    #Operations=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Equipment'
        verbose_name='Оборудование'
        verbose_name_plural='Оборудование'

    def __str__(self) -> str:
        return self.name   

class Amortizations(models.Model):
    equipment=models.ForeignKey(to=Equipments,null=True, verbose_name='Источник', on_delete=models.CASCADE)
    #Operations=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Amortization'
        verbose_name='Амортизация'
        verbose_name_plural='Амортизации'

    def __str__(self) -> str:
        return self.equipment.name   

class OperationsCategories(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #Operations=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='OperationCategory'
        verbose_name='Категория операции'
        verbose_name_plural='Категории операций'

    def __str__(self) -> str:
        return self.name   

class ComponentsTechCategories(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #Projects=models.PositiveIntegerField()
    parent=models.ForeignKey(to='self',null=True, verbose_name='Источник', on_delete=models.CASCADE)#Отображает множество сущностей ComponentTechCategorys на себя
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='ComponentTechCategory'
        verbose_name='Техническая категория компонента'
        verbose_name_plural='Технические категории компонентов'

    def __str__(self) -> str:
        return self.name   

class ComponentsProjCategories(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #Projects=models.PositiveIntegerField()
    parent=models.ForeignKey(to='self',null=True, default=1, verbose_name='Родительская категория', on_delete=models.CASCADE)#Отображает множество сущностей ComponentProjCategorys на себя
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='ComponentProjCategory'
        verbose_name='Проектная категория компонента'
        verbose_name_plural='Проектные категории компонентов'

    def __str__(self) -> str:
        return self.name   

class ComponentsGoals(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #Projects=models.PositiveIntegerField()
    parent=models.ForeignKey(to='self',null=True, verbose_name='Источник', on_delete=models.CASCADE)#Отображает множество сущностей ComponentGoals на себя
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='ComponentGoal'
        verbose_name='Целевое назначение компонента'
        verbose_name_plural='Целевые назначения компонентов'

    def __str__(self) -> str:
        return self.name   

class Components(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    componentTechCategory=models.ForeignKey(to=ComponentsTechCategories,null=True, verbose_name='Техническая категория', on_delete=models.CASCADE)
    componentProjCategory=models.ForeignKey(to=ComponentsProjCategories,null=True, verbose_name='Проектная категория', on_delete=models.CASCADE)
    componentGoal=models.ForeignKey(to=ComponentsGoals,null=True, default=1, verbose_name='Цель', on_delete=models.CASCADE)
    owners=models.ManyToManyField(to="Components",through="ComponentsComponents",through_fields=("ownerComponent","partComponent"), verbose_name='Владелец')#Отображает множество сущностей Components на себя(владельцы)
    source=models.ForeignKey(to=Sources,null=True, verbose_name='Источник', on_delete=models.CASCADE)
    chart=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Чертёж')
    sketch=models.ImageField(upload_to='proj_images',blank=True,null=True,verbose_name='Эскиз')#
    photo=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Фото')
    demonstrableForm=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Наглядное отображение')
    description=models.TextField(max_length=200,blank=True,null=True,verbose_name='Описание')
    сomponentsOperations=models.ManyToManyField(
        to="Operations",
        through="ComponentsOperations",
        through_fields=("component","operation"),
        verbose_name='Операции')
    #multiplier=models.PositiveIntegerField(default=1)
    quantity=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Количество на складе')
    unit=models.ForeignKey(to=Units,null=True, verbose_name='Оценочная единица', on_delete=models.CASCADE)
    #projectComponents=models.ForeignKey(to=Components,null=True, verbose_name='Категория проекта', on_delete=models.CASCADE)
    planTime=models.TimeField(blank=True,null=True)
    startDateTame=models.DateTimeField(blank=True,null=True)
    finishDateTame=models.DateTimeField(blank=True,null=True)
    price=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Стоимость единицы')
    discount=models.DecimalField(default=0.00,max_digits=4,decimal_places=2,verbose_name='Скидка в %')
    selfCost=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Себестоимость')
    #PlanWorks=models.PositiveIntegerField()
    #MakeWorks=models.PositiveIntegerField()
    #RowMaterials=models.PositiveIntegerField()
    #Orders=models.PositiveIntegerField()
    #Works=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Component'
        verbose_name='Компонент'
        verbose_name_plural='Компоненты'
        ordering=("id",)

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    def __str__(self) -> str:
        return self.name 
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price-self.price*self.discount/100 , 2)
        
        return self.price

class ComponentsComponents(models.Model):

    ownerComponent=models.ForeignKey(to=Components, null=True, related_name='parts', verbose_name='Источник', on_delete=models.CASCADE)
    partComponent=models.ForeignKey(to=Components,null=True, related_name='assembles', verbose_name='Источник', on_delete=models.CASCADE)
    quantity=models.DecimalField(default=1.00,max_digits=7,decimal_places=2,verbose_name='Количество')

    class Meta:
        db_table='ComponentsComponent'
        verbose_name='Компонент'
        verbose_name_plural='Компоненты'

    def __str__(self) -> str:
        return self.name 
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price-self.price*self.discount/100 , 2)
        
        return self.price

class Projects(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #projectComponents=models.ForeignKey(to=Components,null=True, verbose_name='Категория проекта', on_delete=models.CASCADE)
    planTime=models.TimeField(blank=True,null=True)
    startDateTame=models.DateTimeField(blank=True,null=True)
    finishDateTame=models.DateTimeField(blank=True,null=True)
    price=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Стоимость')
    discount=models.DecimalField(default=0.00,max_digits=4,decimal_places=2,verbose_name='Скидка в %')
    selfCost=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Себестоимость')
    #PlanWorks=models.PositiveIntegerField()
    #MakeWorks=models.PositiveIntegerField()
    #RowMaterials=models.PositiveIntegerField()
    #Orders=models.PositiveIntegerField()
    #Works=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Project'
        verbose_name='Проект'
        verbose_name_plural='Проекты'

    def __str__(self) -> str:
        return self.name   

    def display_id(self):
        return f"{self.id:09}"  

    def sell_price(self):
        if self.discount:
            return round(self.price*self.discount/100,2)
        return self.price
        
class ProjectsComponents(models.Model):#связь многие ко многим
    component=models.ForeignKey(to=Components,null=True, verbose_name='Категория проекта', on_delete=models.CASCADE)
    project=models.ForeignKey(to=Projects,null=True, verbose_name='Категория проекта', on_delete=models.CASCADE)

    class Meta:
        db_table='ProjectComponent'
        verbose_name='Компонент проекта'
        verbose_name_plural='Компоненты проектов'

    def __str__(self) -> str:
        return self.component.name+" - "+self.project.name   
    
class Operations(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    #сomponentsOperations=models.ForeignKey(to=ComponentsOperations,null=True, verbose_name='Материал', on_delete=models.CASCADE)
    time=models.TimeField(blank=True,null=True)
    unit=models.ForeignKey(to=Units,null=True, verbose_name='Елиница', on_delete=models.CASCADE)
    cost=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Стоимость')
    category=models.ForeignKey(to=OperationsCategories,null=True, verbose_name='Категория операции', on_delete=models.CASCADE)
    equipment=models.ForeignKey(to=Equipments,null=True, verbose_name='Оборудование', on_delete=models.CASCADE)
    multiplier=models.DecimalField(default=1.00,max_digits=7,decimal_places=2,verbose_name='Количество')
    unitTime=models.TimeField()
    salary=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Зарплата')
    #Childs если категория - root
    #ConsumptionComponents=models.PositiveIntegerField() расходные компоненты
    #RetreatRowMaterials=models.PositiveIntegerField() отходы
    amortization=models.ForeignKey(to=Amortizations,null=True, verbose_name='Елиница', on_delete=models.CASCADE)
    #Works=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Operation'
        verbose_name='Операция'
        verbose_name_plural='Операции'

    def __str__(self) -> str:
        return self.name   

class ComponentsOperations(models.Model):# связь многие ко многим
    component=models.ForeignKey(to=Components,null=True, verbose_name='Материал', on_delete=models.CASCADE)
    operation=models.ForeignKey(to=Operations,null=True, verbose_name='Операция', on_delete=models.CASCADE)
    quantity=models.DecimalField(default=1.00,max_digits=7,decimal_places=2,verbose_name='Количество')

    class Meta:
        db_table='ComponentOperation'
        verbose_name='Операция компонента'
        verbose_name_plural='Операции компонентов'

    def __str__(self) -> str:
        return self.component.name+" - "+self.operation.name    

class OperationsStatuses(models.Model):# связь многие ко многим
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='OperationStatus'
        verbose_name='Статус операции'
        verbose_name_plural='Статусы операций'

    def __str__(self) -> str:
        return self.name   

class ProjectsOperations(models.Model):# связь многие ко многим
    project=models.ForeignKey(to=Projects,null=True, verbose_name='Материал', on_delete=models.CASCADE)
    operation=models.ForeignKey(to=Operations,null=True, verbose_name='Операция', on_delete=models.CASCADE)
    operationStatus=models.ForeignKey(to=OperationsStatuses,null=True, verbose_name='Операция', on_delete=models.CASCADE)

    class Meta:
        db_table='ProjectOperation'
        verbose_name='Операция проекта'
        verbose_name_plural='Операции проектов'

    def __str__(self) -> str:
        return self.project.name+" - "+self.operation.name   

class Orders(models.Model):
    dateTime=models.DateTimeField(blank=True,null=True)     
    orderer=models.ForeignKey(to=Orderers,null=True, verbose_name='Заказчик', on_delete=models.CASCADE)
    project=models.ForeignKey(to=Projects,null=True, verbose_name='Проект', on_delete=models.CASCADE)
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Order'
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

    def __str__(self) -> str:
        return self.project.name+" - "+self.orderer.name  

class Workers(models.Model):
    familyName=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    secondName=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    passport=models.CharField(max_length=150,blank=True,null=True)
    dateOfBirth=models.DateTimeField()
    address=models.CharField(max_length=150,blank=True,null=True) 
    telephones=models.CharField(max_length=150,blank=True,null=True) 
    photo=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Фото')
    #Works=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Worker'
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'

    def __str__(self) -> str:
        return self.familyName   

class Works(models.Model):
    startDateTimeOperation=models.DateTimeField(null=False)
    finishtDateTimeOperation=models.DateTimeField(null=True)#если null - операция не завершена
    workTime=models.TimeField(blank=True,null=True)
    worker=models.ForeignKey(to=Workers,null=True, verbose_name='Сотрудник', on_delete=models.CASCADE)
    project=models.ForeignKey(to=Projects,null=True, verbose_name='Проект', on_delete=models.CASCADE)
    operation=models.ForeignKey(to=Operations,null=True, verbose_name='Операция', on_delete=models.CASCADE)
    makeWork=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Сделано работы,с')
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Work'
        verbose_name='Работа'
        verbose_name_plural='Работы'

    def __str__(self) -> str:
        return f'Проект - {self.project.name} Сотрудник - {self.worker.familyName}  Операция - {self.operation.category.name}  {self.operation.co.name} ' 

from datetime import datetime
class Storage(models.Model):
    dateTime=models.DateTimeField(default=datetime.now())     
    component=models.ForeignKey(to=Components,null=True, verbose_name='Материал', on_delete=models.CASCADE)
    quantity=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Количество')
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='Storage'
        verbose_name='На складе'
        verbose_name_plural='На складе'

    def __str__(self) -> str:
        return self.dateTime+" - "+self.component.name    
