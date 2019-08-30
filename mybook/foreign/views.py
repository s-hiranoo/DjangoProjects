from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Question, Choice



def index(request):
    latest_question_list = Question.objects.all().order_by('-created_at')[:5]
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'foreign/index.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question).order_by('choice_text')
    context = {'question': question, 'choices': choices}
    return render(request, 'foreign/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'foreign/results.html', {'question': question})
    #return HttpResponse('Results of question %s' % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'foreign/detail.html',{
                          'question': question,
                          'error_message': "You didn't select your choice. Select a choice and push Vote!"
                      })

    else:
        selected_choice.vote += 1
        selected_choice.save()
        return redirect('foreign:results', question_id=question_id)
    #return HttpResponse('Vote of question %s' % question_id)

