from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from  books.models import Contact
from datetime import datetime



# Create your views here.
def contact(request):
    if request.method =="POST":
         Name = request.POST.get('Name')
         Email = request.POST.get('Email')
         Telephone = request.POST.get('Telephone')
         Subject = request.POST.get('Subject')
         Message = request.POST.get('Message')
         contact = Contact(Name = Name, Email=Email, Telephone=Telephone, Subject= Subject, Message=Message, date=datetime.today())
         contact.save()
    return render(request, 'mail.html')