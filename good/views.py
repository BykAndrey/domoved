from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response,redirect
from .models import Project,Images,Opinion,Question,AboutSite
from .forms import leaveOpinionForm,AskForm
from django.http import Http404
# Create your views here.
#Обязательное поле при рендеринге на страницаъ где есть хлебные крогки.
# хлебные крошки. первый элемент название, второй slug, все slug складываются в url
#    args['Crops']=[['Услуги','service'],[cat.name,cat.slug],[subcat.name,subcat.slug]]


def home(request):
   args={}
   args.update(csrf(request))
   args['askform'] = AskForm
   project=Project.objects.filter(boolVisible=True)[0:3]
   if len(project)>0:
      args['project']=project
   else:
      args['project']=None


   opinions=Opinion.objects.filter(boolVisible=True).order_by('-date')[0:4]
   if len(opinions)>0:
      args['opinions']=opinions
   else:
      args['opinions']=None


   return render_to_response('home.html',args)

def getOpinion(request):
      args={}
      args.update(csrf(request))
      if request.POST:
         form=leaveOpinionForm(request.POST,request.FILES)
         print(request.POST)
         print(request.FILES)

         if form.is_valid():
            print('Valid')
            opinion=Opinion()
            opinion.name=form.cleaned_data['name']
            opinion.email=form.cleaned_data['email']
            opinion.opinion=form.cleaned_data['opinion']
            opinion.image=form.cleaned_data['image']
            #print()
            opinion.save()
            args['WHAT'] = "отзыв!"
            return render_to_response('thank.html', args)
         args['form']=form
         return render_to_response('feedback.html',args)
      args['form']=leaveOpinionForm
      return render_to_response('feedback.html', args)

def AddQuestion(request):
   args = {}
   args.update(csrf(request))

   if request.POST:
      form=AskForm(request.POST)
      if form.is_valid():
         question=form.save()
         args['WHAT']="вопрос!"
         args['Crops']=[['Ответы на вопросы','questions'],['Спасибо','#']]
         return render_to_response('thank.html',args)
      else:
         args['form']=form
         args['Crops']=[['Ответы на вопросы','questions'],['Форма вопроса','add']]
         return render_to_response('askForm.html',args)
   else:
      args['form'] = AskForm
      args['Crops']=[['Ответы на вопросы','questions'],['Форма вопроса','add']]
      return render_to_response('askForm.html',args)
def listproject(request):
   args={}
   args.update(csrf(request))
   args['list']=Project.objects.filter(boolVisible=True)
   args['Crops']=[['Проекты','projects']]
   if args['list']==None:
      return redirect('/')
   return  render_to_response('listProjects.html',args)


def cartofproject(request,url):
   project=Project.objects.filter(slug=url,boolVisible=True).first()
   args={}
   args.update(csrf(request))
   if project != None:
      if project.image != None:
         args['project']=project

      images=Images.objects.filter(project=project)
      if images !=None:
         args['images']=images
      else:
         args['images']="None"


      args['Crops']=[['Проекты','projects'],[project.title,project.slug]]
      return render_to_response('cartofproject.html', args)
   else:
      return redirect('/')



def listopinion(request):
   args={}
   args.update(csrf(request))
   args['opinions']=Opinion.objects.filter(boolVisible=True)
   args['Crops']=[['Отзывы','opinions']]
   return render_to_response('listOpinions.html',args)




def listquestions(request):
   args={}
   args.update(csrf(request))
   args['questions']=Question.objects.filter(boolVisible=True).order_by('-date')
   args['Crops']=[['Ответы на вопросы','questions']]
   return render_to_response('listQuestions.html',args)

def infopage(request,url):
   args={}
   page=AboutSite.objects.filter(url=url).first()
   args['page']=page
   if(args['page']==None):
       raise Http404
   args['Crops']=[[page.title,page.url]]
   return  render_to_response('InfoPage.html',args)

def robot(request):
   return  render_to_response("robots.txt",  content_type='text/plain')

def sitemap(request):
   return  render_to_response("sitemap.xml",  content_type='text/plain')

def google(request):
   return  render_to_response("google8e590507aa68c203.html",{})
