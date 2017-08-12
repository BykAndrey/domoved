"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from .views import *
urlpatterns = [


    url(r'^projects/(?P<url>[-\w]+)/$', cartofproject),
    url(r'^projects/$', listproject,name="ListProjects"),
    url(r'^opinions/$', listopinion, name="ListOpinion"),
    url(r'^feedback/$',getOpinion,name="feedback"),
    url(r'^question/add/$',AddQuestion,name="addquestion"),
    url(r'^questions/$',listquestions,name="ListQuestions"),
    url(r'^info/(?P<url>[-\w]+)/$',infopage,name="infopage"),
    url(r'^robot.txt$',robot)

]
if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True

urlpatterns += staticfiles_urlpatterns()
