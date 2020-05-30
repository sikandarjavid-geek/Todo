from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
#Imports for login logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'tasks/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def TaskList(request):
    tasks = Tasks.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path_info)


    context = {'tasks':tasks, 'form':form}

    return render(request,'tasks/list.html',context)

@login_required
def updatetask(request,pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('list')
    context = {'form':form}
    return  render(request,'tasks/update_tasks.html',context)

@login_required
def deleteTask(request,pk):
    item = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('list')
    
    context = {'item':item}
    return render(request,'tasks/delete.html',context)

def UserProfile(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()    

            profile = profile_form.save(commit=False)
            profile.user = user
             
            if 'profile_pic' in request.FILES:
                 profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,'tasks/registration.html',
        {'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered}) 



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account Not Active")
        
        else:
            print("Someone tried to login and Failed")
            print("Username:{} and password: {}".format(username,password))
            return HttpResponse("Invalid login Details! Try again")


    else:
        return render(request,'tasks/login.html',{})


        

    