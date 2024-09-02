from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Sources

class User(AbstractUser):
    image=models.ImageField(upload_to='users_images',blank=True,null=True,verbose_name='Аватар')
    familyName=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    name=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    secondName=models.CharField(max_length=150,blank=True,null=True,verbose_name='Название')
    enterprise=models.ForeignKey(to=Sources,null=True, verbose_name='Предприятие', on_delete=models.CASCADE)
    dateOfBirth=models.DateTimeField(blank=True,null=True,verbose_name='Дата рождения')
    address=models.CharField(max_length=150,blank=True,null=True) 
    telephones=models.CharField(max_length=150,blank=True,null=True) 
    photo=models.ImageField(upload_to='main_images',blank=True,null=True,verbose_name='Фото')
    #Orders=models.PositiveIntegerField()
    note=models.TextField(max_length=200,blank=True,null=True,verbose_name='Примечания')
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table='user'
        verbose_name='Пользователя'
        verbose_name_plural='Пользователи'

    def __str__(self) -> str:
        return self.username 
    
