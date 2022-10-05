# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from . import forms
from accounts.models import contact
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 



def SignUp(request):
    if request.method=="POST":
      # Get the post parameters
      username=request.POST['username']
      email=request.POST['email']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']

      # check for errorneous input
      if len(pass1)<8:
        messages.warning(request, " Your password must contain 8 characters")
        return redirect('accounts:signup')

      if not username.isalnum():
        messages.warning(request, " User name should only contain letters and numbers")
        return redirect('accounts:signup')

      if User.objects.filter(username=username).exists():
        # messages.error(request,'Choose Unique Title')
        messages.warning(request, ' Choose Unique username')
        return redirect('accounts:signup')


      if (pass1!= pass2):
        messages.warning(request, " Passwords do not match ☺")
        return redirect('accounts:signup')

      
      # Create the user
      myuser = User.objects.create_user(username, email, pass1)
      myuser.save()
      messages.success(request, " Your account has been created successfully !!!")
      return redirect('accounts:login')
    else:
      return render(request, 'accounts/signup.html')

def contactus(request):
  if request.method == 'POST':
    name = request.POST['Username']
    email = request.POST['mailid']
    phoneNo = request.POST['phoneNo']
    issue = request.POST['issue']
    # print(name + email + phoneNo + issue)
    newcontact = contact(name=name, contactNo=phoneNo, email=email, issue=issue)
    newcontact.save()
    messages.success(request, 'We have received Your Mail we will contact You Soon')
  return render(request, 'accounts/contactus.html')



