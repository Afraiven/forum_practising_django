from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! You are now able to login")
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
