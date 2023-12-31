from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def mainPage(request):
    return render(request, 'main.html')

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!= pass2:
            return HttpResponse("Your password and confirm pass is not same. Try again!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render(request, 'signup.html')

def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Your username and passwrod is wrong! Try again!")
    return render(request, 'login.html')

def LogOutPage(request):
    logout(request)
    return redirect('login')


# https://github.com/AminulMahi/Django_Registration_form.git
# https://github.com/AminulMahi/Django_projects.git 