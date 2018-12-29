from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')# dictionary that will give usename
			messages.success(request, f' Account created for {username}!')
			return redirect('index')
	else:
		form=UserRegisterForm()
	return render(request, 'user/register.html', {'form':form})

