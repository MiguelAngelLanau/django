from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'app/index.html')

def hola(request):
    return render(request, 'app/hola.html')
