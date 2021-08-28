from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import forms
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UserCreationForm,LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse,JsonResponse
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



