from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import errors, choice
from django.urls import reverse

from django.views import generic
from django.template import loader


class IndexView(generic.ListView):
    template_name='blogging/index.html'
    cotext_object_name='latest_question_list'

    def get_queryset(self):
        return errors.objects.order_by('-date_posted')[:5]

class DetailView(generic.DetailView):

    model = errors
    template_name = "blogging/detail.html"


class ResultsView(generic.DetailView):
    model = errors
    template_name='blogging/results.html'


def vote(request,question_id):
    question = get_object_or_404(errors, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,choice.DoesNotExist):
        return render(request, "blogging/detail.html", {'question':question, 'error_message':"You didn't select a choice.",})

    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('blogging:results', args=(question.id,)))



