from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import contact
# Create your views here.

# def home(request):
#     return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')
        print(name,email,content,number)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Name should be between 1 and 30 characters')
            request.render(request,'home.html')

        if len(email)>1 and len(email)<30:
            pass        
        else:
            messages.error(request,'Invalid email try again')
            request.render(request,'home.html')

        if len(content)>2 and len(content)<400:
            pass
        else:
            messages.error(request,'Content should be between 2 and 400 characters')
            request.render(request,'home.html')
        if len(number)>1 and len(number)<13:
            pass
        else:
            messages.error(request,'Invalid number')
            request.render(request,'home.html')
        ins=models.contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank you for conacting me|| your message has been sent')
        print('success')
        print('the requet is  no pass')
        
    return render(request,'home.html')