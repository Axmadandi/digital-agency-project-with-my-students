from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.
def index(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def detail(request,id):
    mymembers = Member.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
