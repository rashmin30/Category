from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request , 'main-page/index.html')

    
def superuser(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        return render(request , 'superuser/superuser.html')
    else:
        messages.error(request , 'Permisstions not allowed')
        return redirect('/check_user/')


def user_login(request):
    if 'submit' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username , password)
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request,'Login successfully.')
            return redirect('/check_user/')
        else:
            messages.error(request,'Login invalid.')
            return redirect('/login/')
    return render(request, 'main-page/login_page.html')

def user_logout(request):
    logout(request)
    messages.success(request , 'Logout successfully.')
    return redirect('/login/')


def check_user(request):
    if request.user.is_superuser == True and request.user.is_staff == True and request.user.is_active == True:
        return redirect('/superuser/')
    else:
        messages.error(request , 'User in valid, Please login')
        return redirect('/login/')
