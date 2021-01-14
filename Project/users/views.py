from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic


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


class ProfileView(generic.ListView):
    template_name = 'users/profile.html'
    # name of sth called context object
    context_object_name = 'chosen_user'
    name = "NewUser"

    # func that returns queryset of Questions sorted by publication date
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return User.objects.filter(username=self.kwargs['name']).first()


