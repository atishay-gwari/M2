from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def viewlist(request):
    try:
        data=Profile.objects.filter(user=request.user.id)
        # data=Profile.objects.all()
        print(data)
        context={"data":data}   
    except :
        messages.warning(request,"Nothing found")
        return redirect('view')
    return render(request,'index.html',context)

@login_required(login_url='login')
def addlist(request):
    form=ProfileForm()
    if request.method=="POST":
        data=ProfileForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('view')
    context={"form":form}
    return render(request,'addlist.html',context)
@login_required(login_url='login')
def updateed(request,id):
    mydata=Profile.objects.get(id=id)
    data=ProfileForm(request.POST or None,instance=mydata)
    if data.is_valid():
        data.save()
        messages.success(request, "Task Added Successfully")
        return redirect('view')
    context={"form":data}
    return render(request,'update.html',context)
# @login_required(login_url='login')
def deleteed(request,id):
    data=Profile.objects.get(id=id)
    data.delete()
    messages.success(request, "Task Added Successfully")
    return redirect('view')



def signup(request):
    if request.method == 'POST':
        user =request.POST['Name']
        email=request.POST['email']
        password1=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        if password1 == confirmpassword:
            if not User.objects.filter(username=user).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username = user, email = email, password=password1)
                    user.save()
        return redirect('login')
    return render(request,'signup.html')


def loginuppage(request):
    if request.method=='POST':
        username=request.POST['Name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('view')
        else:
            return redirect('login')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)

    return redirect('view')