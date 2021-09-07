from django.http.response import HttpResponse
from django.shortcuts import render
from books.models import UploadsBook
from django.db.models import Q
# Create your views here.
#  get_type_book_and_qty_number
def bookAndQty():
    get_name = UploadsBook.objects.values('Types_of_Book' )
    print(dir(UploadsBook.objects))
    get_qty = UploadsBook.objects.values('Quantity')
    print(get_name)
    print(get_qty)


def showChart(request):
    bookAndQty()
    return HttpResponse("done")
