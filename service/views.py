from django.shortcuts import render,render_to_response,redirect

# Create your views here.
#Обязательное поле при рендеринге. хлебные крошки. первый элемент название, второй slug, все slug складываются в url
#    args['Crops']=[['Услуги','service'],[cat.name,cat.slug],[subcat.name,subcat.slug]]
from .models import *

def listCategoryService(request):
    args={}
    args['title'] = "Наши услуги"
    args['category']=Category.objects.filter(boolShowOnMain=True,boolVisible=True)

    args['subcategory'] = SubCategory.objects.filter(boolShowOnMain=True, boolVisible=True)
    #args['service'] = Service.objects.filter(boolShowOnMain=True, boolVisible=True)
    args['Crops']=[['Услуги','service'],]
    return  render_to_response("listService.html",args)

def CategoryService(request, url):
    args={}
    main=Category.objects.filter(boolVisible=True,slug=url).first()
    if main==None:
        return redirect('/service')
    args['title']=main.title
    args['namePage'] = main.name
    args['basecat']=main
    args['category']=SubCategory.objects.filter(boolVisible=True,category=main)
    args['subcategory']=None
    args['Crops']=[['Услуги','service'],[main.name,main.slug]]
    return render_to_response("listService.html", args)




def Services(requeste,url,suburl):
    args = {}

    subcat=SubCategory.objects.filter(slug=suburl).first()
    cat=subcat.category
    if subcat is not None:
        args['title']=subcat.title
        args['subcat']=subcat
        args['services']=Service.objects.filter(category=subcat)
        args['images']=ImagesSub.objects.filter(category=subcat)
        args['namePage'] = subcat.name
        args['Crops']=[['Услуги','service'],[cat.name,cat.slug],[subcat.name,subcat.slug]]
    else:
        args['title'] = "Извините, запрошенный адресс не существует"
    return render_to_response("Services.html", args)
