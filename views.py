from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Register
from django.http import HttpResponse

@csrf_exempt
def home(request):
    if request.method == 'POST':
        
        register = Register()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        register.name = name
        register.email = email
        register.phone =phone 
        register.message = message
        register.save()
        
        return redirect('/')
        
        # return HttpResponse("<h1>Thaks Fill the Registration Form <br>Then Visit Website for free Templates</h1>")
    return render(request ,'index.html')

def contact(request):
    return render(request , 'contact.html')

def why_us(request):
    return render(request ,'why.html')

def trainer(request):
    return render(request ,'trainer.html')
