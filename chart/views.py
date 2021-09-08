from django.http.response import JsonResponse
from django.shortcuts import render
from books.models import UploadsBook
import random
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


#parameter 'l' => length of the dictonary returned form the bookAndQty function 
def generating_different_color_function(l):
    rgb_list = []
    for _ in range(l):
        r = str(random.randint(0,256))
        g = str(random.randint(0,256))
        b = str(random.randint(0,256))
        rgb = f'rgb({r},{g},{b})'
        rgb_list.append(rgb)
    return rgb_list


def showChart(request):
    name_qty = bookAndQty()
    color_list = generating_different_color_function(len(name_qty))
    print(color_list)
    return render(request,'chart.html',context={'color':color_list,'name':name_qty})


