from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Choice, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import request
# Create your views here.

def vote(request, question_id):
    
    p = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
                                                     'question' : p,
                                                     'error_message': "you didn't select a choice"
                                                     })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', arg=(p.id)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})