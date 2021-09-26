from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from books.models import Contact
from datetime import datetime
from .forms import AddProductForm
from .models import UploadsBook


# Create your views here.
def contact(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Telephone = request.POST.get('Telephone')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')
        contact = Contact(Name=Name, Email=Email, Telephone=Telephone,
                          Subject=Subject, Message=Message, date=datetime.today())
        contact.save()
    return render(request, 'mail.html')


def addproduct(request):
    return render(request, 'addproduct.html')

# This function will add new book.


def add(request):
    if request.method == 'POST':
        afm = AddProductForm(request.POST, request.FILES)
        if afm.is_valid():
            #     isbn = afm.cleaned_data['isbn']
            #     bn = afm.cleaned_data['Book_Name']
            #     an = afm.cleaned_data['Author_Name']
            #     dm = afm.cleaned_data['Description']
            #     rd = afm.cleaned_data['ReleaseDate']
            #     sp = afm.cleaned_data['Selling_price']
            #     Label = afm.cleaned_data['Label']
            #     pb = afm.cleaned_data['Publication']
            #     tb = afm.cleaned_data['Types_of_Book']
            #     qt = afm.cleaned_data['Quantity']
            #     img = afm.cleaned_data['Image']
            #   #   spn = afm.cleaned_data['Seller_phoneno']
            #   #   sa = afm.cleaned_data['Seller_address']
            #   #   reg = AddProductForm(isbn=isbn, Book_Name=bn, Author_Name=an, Description=dm, ReleaseDate=rd, Selling_price=sp,
            #   #                        Label=Label, Publication=pb, Types_of_Book=tb, Quantity=qt, Image=img, Seller_phoneno=spn, Seller_address=sa)
            #     reg = AddProductForm(isbn=isbn, Book_Name=bn, Author_Name=an, Description=dm, ReleaseDate=rd, Selling_price=sp,
            #                          Label=Label, Publication=pb, Types_of_Book=tb, Quantity=qt, Image=img)
            afm.save()
            afm = AddProductForm()
    else:
        afm = AddProductForm()
    return render(request, 'add.html', {'form': afm})

# This function will show all added book.


def view(request):
    allbooks = UploadsBook.objects.all()
    print(allbooks)
    print("HEllo")
    return render(request, 'view.html', {'allbooks': allbooks})

# This function will delete book data


def delete_book(request, id):
    if request.method == 'POST':
        delb = UploadsBook.objects.get(pk=id)
        delb.delete()
        return HttpResponseRedirect('/view')


# This function will edit the book details


def update_book(request, id):
    if request.method == 'POST':
        updatebook = UploadsBook.objects.get(pk=id)
        ufm = AddProductForm(request.POST, instance=updatebook)
        if ufm.is_valid():
            ufm.save()
    else:
        updatebook = UploadsBook.objects.get(pk=id)
        ufm = AddProductForm(instance=updatebook)

    return render(request, 'update.html', {'form': ufm})
