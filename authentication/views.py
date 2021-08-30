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
        fname = request.POST.get('first_name')

        if form.is_valid():
            if User.objects.filter(email=email).exists():
               return JsonResponse({"error_email":"Email already exists"}) 
            else:
                email = form.cleaned_data['email']
                otp = sendEmail(email,fname)
                dt = PreRegistration(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username= form.cleaned_data['username'],email=email,otp=otp,password1 = form.cleaned_data['password1'],password2 = form.cleaned_data['password2'])
                dt.save()
                # form.save()
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
    for i in range(6):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email,fname):

    otp = creatingOTP()
    email_message =   f"""
Dear Sir/Madam,
{fname}
ATTN : Please do not reply to this email.This mailbox is not monitored and you will not receive a response.

Your One Time Password (OTP ) is {otp}.

If you have any queries, Please contact us at,

किताब खाना,
Thali,Kathmandu, Nepal.
Phone # 977-01-4255306
Email Id: kitabkhana55@gmail.com

Warm Regards,
Kitab Khana Limited."""
    send_mail(
    'One Time Password',
    email_message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return otp

def verifyUser(request):
    # if not request.user.is_authenticated:
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            if form.is_valid():
                otp1 = form.cleaned_data['first']
                otp2= form.cleaned_data['second']
                otp3 = form.cleaned_data['third']
                otp4 = form.cleaned_data['fourth']
                otp5 = form.cleaned_data['fifth']
                otp6 = form.cleaned_data['sixth']
                otp = f"{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}"
                data = PreRegistration.objects.filter(otp = int(otp))
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
                    print('success')
                    return HttpResponseRedirect('/verify/')   
                else:
                    messages.success(request,'Entered OTO is wrong')
                    return HttpResponseRedirect('/reg_show/')
        else:            
            form = VerifyForm()
        return render(request,'otp.html',{'form':form})
    # else:
    #     return HttpResponseRedirect('/')

