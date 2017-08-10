from django import template
from slider.models import Slide
register = template.Library()


@register.inclusion_tag("slider.html")
def slider():
    args={}
    args['count']=(Slide.objects.filter(boolVisible=True)).count()
    args['slides']=Slide.objects.filter(boolVisible=True)
    return args