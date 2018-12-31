
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UserRegisterForm

def home(request):
    return render(request,'polls/home.html')



def index(request, *args):
    latest_question_list = Question.objects.order_by('-pub_date')
    paginator = Paginator(latest_question_list, 1)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'polls/index.html',{'questions': questions})
		 



def results(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/results.html', {'question': question})

		
def vote(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')# dictionary that will give usename
			messages.success(request, f' Account created for {username}!')
			return redirect('polls:polls-index')
	else:
		form=UserRegisterForm()
	return render(request, 'polls/register.html', {'form':form})


