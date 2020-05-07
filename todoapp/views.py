from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):

    return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm()})
