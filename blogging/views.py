from django.shortcuts import render
from django.http import Http404
# Create your views here.

from django.http import HttpResponse
from .models import errors

from django.template import loader



def detail(request,question_id):
    return HttpResponse("You are looking at question %s ." %question_id)

def results(request , question_id):
    response="You are lookig at the results of question %s ."
    return HttpResponse(response %question_id)

def vote(request , question_id):
    return HttpResponse("You're voting on question %s ." %question_id)

def index(request):
    latest_questions_list = errors.objects.order_by('-date_posted')[:5]
    context = { 'latest_questions_list':latest_questions_list,}

    return render(request,'blogging/index.html',context)

def detail(request , question_id):

    question = get_object_or_404(errors,pk=question_id)

    return render(request,'blogging/detail.html',{'question':question})