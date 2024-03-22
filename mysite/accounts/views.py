from django.shortcuts import render, redirect
from blog.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def signup_view(request):
    # if the request is passing information, change the logic
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # if the form information is valid, save it to the DB
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('blog:posts')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
