from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BookingAppointmentsForm,query_form,subscriptionForm
from .models import package
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
# Create your views here.
def Home(request):
    return render(request,"Health/index.html")
    

def about_us(request):  
    return render(request,"Health/about.html")

def gallery(request):  
    return render(request,"Health/gallery.html")

def Blogs(request):  
    return render(request,"Health/blog.html")

def contact(request):  
    form=query_form()
    if request.method == "POST":
     form = query_form(request.POST)    
     if form.is_valid:
        form.save()
        return redirect('query_confirmations')
    var={'form':form}
    return render(request,"Health/contact.html",var)

def appointment(request):  
    form=BookingAppointmentsForm()
    if request.method == "POST":
     form = BookingAppointmentsForm(request.POST)    
     if form.is_valid:
        form.save()
        return redirect('booking_cnfrm')
    var={'form':form}
    return render(request,"Health/appointment.html",var)

def loginUser(request):  
    return render(request,"account/login.html")

def registerUser(request):  
    return render(request,"account/registration.html")

def profile(request):  
    return render(request,"account/profile.html")

def booking_cnfrm(request): 
     
    return render(request,"Health/appconf.html")

def query_confirmations(request): 
     
    return render(request,"Health/queryconf.html")

def subscription(request):
    pkg=package.objects.all()
    form=subscriptionForm()
    if request.method == "POST":
     form = subscriptionForm(request.POST)    
     if form.is_valid:
        form.save()
        return redirect('subscnf')
     else:
         messages.error(request,"Email already exist")
    var={'form':form,'pkg':pkg}
    return render(request,"Health/packagereg.html",var)

def subscnf(request):
    return render(request,"Health/subscnf.html")


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == 'POST':
        username = request.POST['username'] 
        password =request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username does not exist")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,"User not found")

    return render(request, 'account/login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')