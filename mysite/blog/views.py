from django.shortcuts import render
from .models import Post, CustomUser
# Create your views here.

def index(request):
    """View function for website homepage"""

    # Prints the amount of posts
    num_posts = Post.objects.all().count()

    # Prints the amount of users
    num_users = CustomUser.objects.all().count()

    context = {
        'num_users' : num_users,
        'num_posts' : num_posts,
    }
    
    # Render the HTML template index.html with information within context
    return render(request, 'index.html', context=context)