from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_in(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('marketing:store')
    else:
        messages.error(request, 'username or password does not exist!')
    return render(request, 'users/login.html')

def sign_out(request):
    logout(request)
    return redirect('marketing:store')

def sign_up(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('marketing:store')
    else:
        messages.error(request, 'an error occured during registration!')
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})