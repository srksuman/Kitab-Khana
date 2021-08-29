from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import forms
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UserCreationForm,LoginForm,VerifyForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import PreRegistration
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
# def registerFunction(request):
#     if not request.user.is_authenticated:
#         if request.method =="POST":
#                 form = UserCreationForm(request.POST)
#                 if form.is_valid():
#                     form.save()
#                     messages.success(request,"Account is created successfully!")
#                     return HttpResponseRedirect('')
#                 else:
#                     log = LoginForm(request = request,data = request.POST)

#         else:  
#             form = UserCreationForm()
#         return render(request,"login.html",{'form':form})
#     else:
#         return HttpResponse("hello")

def index_page(request):
    return render(request,'index.html')

# def loginFunction(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = LoginForm(request = request,data = request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 pas = form.cleaned_data['password']
#                 usr = authenticate(username=username,password = pas)
#                 login(request,usr)
#                 messages.success(request,"Account is created successfully!")
#                 return HttpResponse("Login success")
#         else:
#             form = LoginForm()
#         return render(request,"login.html",{'form':form})
#     else:
#         return HttpResponse("Login") 


# def signin_signup_function(request):
#     if request.method == 'POST':
#         if 'reg_form' in request.POST:
#             userCreation = UserCreationForm(request.POST)
#             if userCreation.is_valid():
#                 userCreation.save()
#                 messages.success(request,"Account is created successfully!")
#                 return HttpResponseRedirect('/')
#             else:
#                 loginForm = LoginForm(request = request,data = request.POST)
#         if 'login' in request.POST:
#             log = LoginForm(request = request,data = request.POST)
#             if log.is_valid():
#                 username = log.cleaned_data['username']
#                 pas = log.cleaned_data['password']
#                 usr = authenticate(username=username,password = pas)
#                 print(usr,username)
#                 login(request,usr)
#                 return HttpResponse("Login success")
#             else:
#                 forms = UserCreationForm(request.POST)
#     else:
#         userCreation = UserCreationForm()
#         loginForm = LoginForm()
#     return render(request,'login.html')


def signup_function(request):
    userCreation = UserCreationForm()
    loginForm = LoginForm()
    return render(request,'login.html',{'userCreation':userCreation,'loginForm':loginForm})

def signup_ajax_function(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        print(email)
        if form.is_valid():
            print("suman raj khanal is good inside view function")
            if User.objects.filter(email=email).exists():
               return JsonResponse({"error_email":"Email already exists"}) 
            else:
                form.save()
                return JsonResponse({"status":200})      
        else:
            error_name =[]
            error_value = []
            for i,j in form.errors.as_data().items():
                print(i,j[0])
                for m in j[0]:
                    error_value.append(m)
                error_name.append(i)
                
            print(form.errors.as_data())
            error = form.errors.as_data()
            return JsonResponse({"status":"errors","error_name":error_name,"error_value":error_value})
    else:
        return JsonResponse({"status":"Failed"})

def signin_ajax_function(request):
    if request.method == 'POST':
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            try:
                usr = authenticate(username=username,password = pas)
            except:
                return JsonResponse({'status':203})
            login(request,usr)
            return JsonResponse({'status':200})     
            
        else:
            error_name =[]
            error_value = []
            for i,j in form.errors.as_data().items():
                print(i,j[0])
                for m in j[0]:
                    error_value.append(m)
                error_name.append(i)
                
            print(form.errors.as_data())
            error = form.errors.as_data()
            return JsonResponse({"status":"errors","error_name":error_name,"error_value":error_value})
    else:
        return JsonResponse({"status":"Failed"})


def creatingOTP():
    otp = ""
    for i in range(11):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email):
    otp = creatingOTP()
    send_mail(
    'One Time Password',
    f'Your OTP pin is {otp}',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return otp

def verifyUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            if form.is_valid():
                otp = form.cleaned_data['otp']
                data = PreRegistration.objects.filter(otp = otp)
                if data:
                    username = ''
                    first_name = ''
                    last_name = ''
                    email = ''
                    password1 = ''
                    for i in data:
                        print(i.username)
                        username = i.username
                        first_name = i.first_name
                        last_name = i.last_name
                        email = i.email
                        password1 = i.password1

                    user = User.objects.create_user(username, email, password1)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    data.delete()
                    messages.success(request,'Account is created successfully!')
                    return HttpResponseRedirect('/verify/')   
                else:
                    messages.success(request,'Entered OTO is wrong')
                    return HttpResponseRedirect('/verify/')
        else:            
            form = VerifyForm()
        return render(request,'html/verify.html',{'form':form})
    else:
        return HttpResponseRedirect('/success/')

