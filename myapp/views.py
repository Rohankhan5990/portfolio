from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        added_date = Contact(name=name,email=email,phone=phone,about=about,added_date=datetime.today())
        added_date.save()
    return render(request,'contact.html')
