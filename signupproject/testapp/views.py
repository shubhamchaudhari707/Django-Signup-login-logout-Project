from django.shortcuts import render,redirect
from .forms import SignupForm , Editform ,Adminform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            fm = Editform(request.POST , instance=request.user)
            if fm.is_valid():
                messages.info(request, 'profile Updated ')
                fm.save()

        else:
            if request.user.is_superuser == True:
                fm = Adminform(instance=request.user)
            else:
                fm =Editform(instance=request.user)

        return render(request, 'testapp/home.html',{'form':fm})

    else:
        return render(request, 'testapp/home.html')

def signups(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request,'Signup created successfully')
            return redirect('login')
            # print(request.POST.get('username'))
            # print(request.POST.get('first_name'))
            # print(request.POST.get('password2'))
    else:
        fm = SignupForm()
    return render(request,'testapp/signup.html',{'form':fm})


def logins(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request , data=request.POST)
            print("fm is valid", fm.is_valid())
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname ,password=upass)
                print(user)
                login(request, user)
                messages.info(request, 'Login Suessfully !!')
                return redirect('home')
            else:
                print("invalid cred")
                messages.info(request, 'invailid credentials ')
                return redirect('login')
        else:
            fm = AuthenticationForm()
        return render(request,'testapp/login.html' ,{'form':fm})

    else:
        return redirect('home')


def logouts(request):
    logout(request)
    return redirect('login')



