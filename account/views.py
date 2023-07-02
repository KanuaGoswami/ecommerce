from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from .forms import UserForm, SellerForm,LoginForm
from .models import customUser

# Create your views here.

def index(request):
    return render(request,'index.html')
def user_register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(email)
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            print(address)
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            # form.save()
            user = customUser.objects.create(username=username,email=email,phone=phone,address=address,password=password,role=role)
            user.set_password(password)
            user.save()

            return HttpResponse("/thanks/")
    return render(request,'user.html',{'form':form})

def seller_register(request):
    form = SellerForm()
    if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(email)
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            print(address)
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            # form.save()
            user = customUser.objects.create(username=username,email=email,phone=phone,address=address,password=password,role=role)
            user.set_password(password)
            user.save()
            # return redirect)

    return render(request,'seller.html',{'form':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = authenticate(phone=phone,password=password)
            if user is not None:
                request.session['phone'] = phone
                return redirect('/dashboard')
            # else:
            #     raise


             

    return render(request,'login.html',{'form':form})
