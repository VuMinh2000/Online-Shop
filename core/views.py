from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.views import View
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact


class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!!")
            return redirect("signpage:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="signinpage/index.html", context={"register_form": form})


def signup_request(request):
    return render(request, 'signinpage/signup.html')
