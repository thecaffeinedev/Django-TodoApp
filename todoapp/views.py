from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def signupuser(request):
    if request.method== 'GET':
        return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm(), 'error':'The username has already been choosen. please choose other'})
        else:
            # tell the user password didnt match
            return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm(), 'error':'Password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodos')
      


def home(request):
    return HttpResponse("Home")