from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from .models import Images,Project,Opinion,Question,AboutSite
# Register your models here.
class ImageInline(admin.TabularInline):
    model = Images
    extra = 1
class ProjectForm(ModelForm):
    class Meta:
        widgets={
            'description':RedactorWidget(editor_options={'lang':'ru'})
        }

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImageInline]
admin.site.register(Project,ProjectAdmin)



@admin.register(Opinion)
class OpinitonAdmin(admin.ModelAdmin):
    list_display =['name','date','boolVisible']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'boolVisible']





class AboutSiteForm(ModelForm):
    class Meta:
        widgets={
            'text':RedactorWidget(editor_options={'lang':'ru'})
        }
@admin.register(AboutSite)
class AboutSiteAdmin(admin.ModelAdmin):
    form = AboutSiteForm
    list_display = ['title',]