from django.shortcuts import render

# Create your views here.
def registerfrontend(request):
    context = {}
    return render(request, 'main.html', context)
