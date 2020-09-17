from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.shortcuts import render, redirect
from accounts.forms import RegisterForm

def signin(request):
	return render(request, 'signin.html')
# Create your views here.
def signup(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    # return redirect("/home")
    else:
	    form = RegisterForm()

    return render(response, "signup.html", {"form":form})
