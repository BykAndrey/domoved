from django.contrib import admin

# Register your models here.
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget

from .models import Category,SubCategory, Service,Material,PriceUnit,ImagesSub

class ServiceForm(ModelForm):
    class Meta:
        exclude=['slug']
class ServiceTab(admin.StackedInline):
    form = ServiceForm
    model = Service
    extra = 0
    verbose_name_plural = 'Услуги'
    suit_classes = 'suit-tab suit-tab-service'

class ImagesSubStacked(admin.StackedInline):
    model = ImagesSub
    extra=0
    verbose_name = "Изображения"
    suit_classes = 'suit-tab suit-tab-images'



class SubCategoryForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'ru'})
        }


class SubCategoryAdmin(admin.ModelAdmin):
    form=SubCategoryForm
    inlines = [ServiceTab,ImagesSubStacked]
    list_display = ['name']
    prepopulated_fields = {
        'slug': ('name',),
    }

    suit_classes='suit-tab suit-tab-general'

    suit_form_tabs=(('general','Категория'),
                    ('service','Услуги'),
                    ('images','Изображения'))
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'category',
                'name',
                'metaDescription',
                'keywords',
                'description',
                'slug',
                'image',
                'boolVisible',
                'boolShowOnMain',

            ]
        })
    ]
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Service)
admin.site.register(Material)
admin.site.register(PriceUnit)