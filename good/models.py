from django.db import models
import uuid
from django.conf import settings
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill


def make_upload_path(instance, filename, prefix=False):
    """
    Create unique name for image or file.
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    f = parts[-1]
    filename = new_name + '.' + f
    return u"%s/%s" % ("images/", filename)


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=180, default="Название проекта", verbose_name="Название")
    metadescription = models.CharField(max_length=180, verbose_name="Meta description", default="def")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="Описание", verbose_name="Описание")
    image=models.ImageField(upload_to=make_upload_path,
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
    slug = models.SlugField(unique=True,default='')
    boolVisible = models.BooleanField(default=False,verbose_name="Опублковать")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Images(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(default="Name", max_length=25)
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default='',
        verbose_name="Image"
    )
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(840, 500)],
                                 format='JPEG',
                                 options={'quality': 60})












#Отзывы
class Opinion(models.Model):
    date=models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    name=models.CharField(default="Name",verbose_name="ФИО", max_length=40)
    email=models.EmailField(verbose_name="Email",default="")
    opinion=models.CharField(default="",verbose_name="Отзыв", max_length=150)
    image=models.ImageField(upload_to=make_upload_path,
        blank=True,verbose_name="Фото проекта")
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(250, 250)],
                                 format='JPEG',
                                 options={'quality': 60})


    boolVisible=models.BooleanField(default=False,verbose_name="Опубликовать")
    class Meta:
        verbose_name_plural="Отзывы"
        verbose_name="Отзыв"


class Question(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    name = models.CharField(default="Name", verbose_name="ФИО", max_length=40)
    email = models.EmailField(verbose_name="Email", default="")
    question=models.TextField(verbose_name="Ваш вопрос",default="Напишите Ваш вопрос")
    answer= models.TextField(default="Ответ", verbose_name="Ответ")
    telephone=models.CharField(default="+7 (123) 456-7891", verbose_name="Телефон", max_length=18)
    boolVisible=models.BooleanField(default=False,verbose_name="Опубликовать")
    class Meta:
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"




# Страницы О компании, Порядок оказания услуг


class AboutSite(models.Model):
        title=models.CharField(verbose_name="Title", default="Title", max_length=180)
        url=models.CharField(verbose_name="URL",default="aboutcompany",max_length=25)
        metaDescription=models.CharField(default="Title", max_length=180)
        text=models.TextField(default=" ",verbose_name="Текст")
        class Meta:
            verbose_name="Page"
            verbose_name_plural="Pages"