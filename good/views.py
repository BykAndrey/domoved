from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response,redirect
from .models import Project,Images,Opinion,Question,AboutSite
from .forms import leaveOpinionForm,AskForm
# Create your views here.



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
         form=leaveOpinionForm(request.POST)
         if form.is_valid():
            opinion=form.save()
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
         return render_to_response('thank.html',args)
      else:
         args['form']=form
         return render_to_response('askForm.html',args)
   else:
      args['form'] = AskForm
      return render_to_response('askForm.html',args)
def listproject(request):
   args={}
   args.update(csrf(request))
   args['list']=Project.objects.filter(boolVisible=True)
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
      return render_to_response('cartofproject.html', args)
   else:
      return redirect('/')



def listopinion(request):
   args={}
   args.update(csrf(request))
   args['opinions']=Opinion.objects.filter(boolVisible=True)
   return render_to_response('listOpinions.html',args)




def listquestions(request):
   args={}
   args.update(csrf(request))
   args['questions']=Question.objects.filter(boolVisible=True).order_by('-date')
   return render_to_response('listQuestions.html',args)

def infopage(request,url):
   args={}
   args['page']=AboutSite.objects.filter(url=url).first()

   return  render_to_response('InfoPage.html',args)

def robot(request):
   return  render_to_response("robot.txt",  content_type='text/plain')