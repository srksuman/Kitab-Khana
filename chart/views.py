from django.http.response import JsonResponse
from django.shortcuts import render
from books.models import UploadsBook
from django.db.models import Q
# Create your views here.
#  get_type_book_and_qty_number
def bookAndQty():
    name_qty = {}
    get_name = UploadsBook.objects.all()
    for i in get_name:
        if i.Types_of_Book not in name_qty:
            name_qty[i.Types_of_Book] = i.Quantity
        else:
            name_qty[i.Types_of_Book] += i.Quantity
    return name_qty
    

def showChart(request):
    name_qty = bookAndQty()
    print(name_qty)
    return JsonResponse(name_qty)
