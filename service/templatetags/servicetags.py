from django import template
from service.models import Category,SubCategory
register = template.Library()



@register.inclusion_tag("footerListService.html")
def footerListService():
    args={}
    category=Category.objects.filter(boolVisible=True)[0:5]
    args['category']=category

    if category.count()<5:
        count=5-category.count()

        args['subcategory']=SubCategory.objects.filter(boolVisible=True, boolShowOnMain=True)[0:count]
    return args