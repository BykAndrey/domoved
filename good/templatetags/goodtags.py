from django import template

register = template.Library()




@register.inclusion_tag("goodItem/goodItemtemplate.html")
def goodItem(good,side):
    coll=side%2
    if coll==0:
        gside = 'left'
    else:
        gside='right'
    if len(good.description)>287:
           good.description=good.description[0:285]+'...'

    return {'good':good,'side':gside}


@register.inclusion_tag("opinionItem.html")
def opinionItem(opinion,side):
    coll=side%2
    if coll==0:
        gside = 'right'
    else:
        gside='left'


    return {'opinion':opinion,'side':gside}