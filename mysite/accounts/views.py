from django.shortcuts import render, redirect
from blog.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    # if the request is passing information, change the logic
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # if the form information is valid, save it to the DB
        if form.is_valid():
            user = form.save()
            login(request,user)
            # log the user in
            return redirect('blog:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:index')
