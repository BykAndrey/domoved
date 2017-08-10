from django.db import models
from service.models import SubCategory
# Create your models here.

class Slide(models.Model):
    name=models.CharField(max_length=25,default="Услуга",verbose_name="Услуга")
    text=models.CharField(max_length=300,default="Описание услуги", verbose_name="Описание услуги")
    prop1 = models.CharField(max_length=33, default="Свойство", verbose_name="Свойство 1",blank=True)
    prop2 = models.CharField(max_length=33, default="Свойство", verbose_name="Свойство 2",blank=True)
    prop3 = models.CharField(max_length=33, default="Свойство", verbose_name="Свойство 3",blank=True)
    prop4 = models.CharField(max_length=33, default="Свойство", verbose_name="Свойство 4",blank=True)

    subcat=models.ForeignKey(SubCategory,blank=True,default=1,verbose_name="Ссылка на услугу")
    boolVisible=models.BooleanField(default=False,verbose_name="Опубликовать")
    class Meta:
        verbose_name="Слайд"
        verbose_name_plural="Слайды"
    def __str__(self):
        return self.name