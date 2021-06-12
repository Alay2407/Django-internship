from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import student
from .models import Data


def home(request):
    return render(request,'home.html')

def contact(request):
   
    if request.method == "POST":
        print("This Is a post")
    
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        fees=request.POST.get('fees')
        number=request.POST.get('number')
        gender=request.POST.get('gender')
        data = Data(fname=fname,lname=lname,fees=fees,number=number,gender=gender)
        data.save()
        print('Data is submited ')

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def myform(request):
    return render(request,'myform.html')
 
def process(request):
    print('welcome')
    print(request.method)
    print(request.POST)
    a=int(request.POST['txt1'])
    b=int(request.POST['txt2'])
    c=a+b
    print(c)
    return render(request,'ans.html',{'mya':a,'myb':b,'mysum':c})


class studentlist(ListView):
   model = student
   template_name = 'slist.html'
# Create your views here.

