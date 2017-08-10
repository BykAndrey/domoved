from django.db import models
from django.utils.text import slugify
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill

from good.models import make_upload_path
# Create your models here.





class BaseCategory(models.Model):
        name = models.CharField(default="Название категории/услуги", max_length=50, verbose_name="Название категории/услуги")
        boolVisible = models.BooleanField(default=False, verbose_name="Опубликовать")
        metaDescription = models.CharField(default="Категория", max_length=50, verbose_name="meta Description")
        boolShowOnMain = models.BooleanField(default=False, verbose_name="Публиковать вместе с категориями")

        slug = models.CharField(unique=True, default='',max_length=200)

        class Meta:
            abstract = True

class Category(BaseCategory):
    description=models.CharField(default="", max_length=300,verbose_name="Описание")
    boolShowOnMain = models.BooleanField(default=False, verbose_name="Публиковать вместе с категориями")
    image = models.ImageField(upload_to=make_upload_path,
                              blank=True,
                              default='',
                              verbose_name="Картинка")
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(250, 250)],
                                 format='JPEG',
                                 options={'quality': 60})
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(840, 500)],
                                 format='JPEG',
                                 options={'quality': 60})
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return self.name


class SubCategory(BaseCategory):
    category=models.ForeignKey(Category,default=1)
    description=models.TextField(default="",verbose_name="Комплектация")
    image = models.ImageField(upload_to=make_upload_path,
                              blank=True,
                              default='',
                              verbose_name="Картинка")
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(250, 250)],
                                 format='JPEG',
                                 options={'quality': 60})
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(840, 500)],
                                 format='JPEG',
                                 options={'quality': 60})
    class Meta:
        verbose_name="Подкатегория"
        verbose_name_plural="Подкатегории"

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(default="Материал", max_length=50, verbose_name="Материал")
    class Meta:
        verbose_name="Материал"
        verbose_name_plural="Материалы"

    def __str__(self):
        return self.name

class PriceUnit(models.Model):
    name = models.CharField(default="Стоимость проекта/м^2", max_length=50, verbose_name="Стоимость проекта/м^2")

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Едицы измерения"

    def __str__(self):
        return self.name



class Service(BaseCategory):
    category=models.ForeignKey(SubCategory)
    duration=models.CharField(default="от 1 до 99 недель", max_length=30, verbose_name="Сроки")
    material=models.ForeignKey(Material,verbose_name="Основной материал")
    price=models.IntegerField(default=1,verbose_name="Стоимость от")
    priceunit=models.ForeignKey(PriceUnit,null=True,verbose_name="Единица измерения")
    class Meta:
        verbose_name_plural="Услуги"
        verbose_name="Услуга"

    def __str__(self):
        return self.name


    def save(self, *args,**kwargs):
        self.slug=slugify(self.name)
        super(Service, self).save(*args,**kwargs)




class ImagesSub(models.Model):
    category = models.ForeignKey(SubCategory)
    name = models.CharField(default="Name", max_length=25)
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default='',
        verbose_name="Image"
    )
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(250, 250)],
                                 format='JPEG',
                                 options={'quality': 60})
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(840, 500)],
                                 format='JPEG',
                                 options={'quality': 60})
