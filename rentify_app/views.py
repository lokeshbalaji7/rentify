from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, PropertyForm
from .models import Property
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('home')  # assuming 'home' is your homepage URL name
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
