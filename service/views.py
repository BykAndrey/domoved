from django.shortcuts import render,render_to_response,redirect

# Create your views here.

from .models import *

def listCategoryService(request):
    args={}
    args['title'] = "Наши услуги"
    args['category']=Category.objects.filter(boolShowOnMain=True,boolVisible=True)
    args['subcategory'] = SubCategory.objects.filter(boolShowOnMain=True, boolVisible=True)
    #args['service'] = Service.objects.filter(boolShowOnMain=True, boolVisible=True)

    return  render_to_response("listService.html",args)

def CategoryService(request, url):
    args={}
    main=Category.objects.filter(boolVisible=True,slug=url).first()

    args['title'] = main.name
    args['basecat']=main
    args['category']=SubCategory.objects.filter(boolVisible=True,category=main)
    args['subcategory']=None
    return render_to_response("listService.html", args)




def Services(requeste,url,suburl):
    args = {}

    subcat=SubCategory.objects.filter(slug=suburl).first()
    if subcat is not None:
        args['subcat']=subcat
        args['services']=Service.objects.filter(category=subcat)
        args['images']=ImagesSub.objects.filter(category=subcat)
        args['title'] = subcat.name
    else:
        args['title'] = "Извините, запрошенный адресс не существует"
    return render_to_response("Services.html", args)