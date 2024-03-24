from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, CustomUser
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def index(request):
    """View function for website homepage"""

    # Prints the amount of posts
    num_posts = Post.objects.all().count()

    # Prints the amount of users
    num_users = CustomUser.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_users' : num_users,
        'num_posts' : num_posts,
    }
    
    # Render the HTML template index.html with information within context
    return render(request, 'index.html', context=context)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'post_list'

class PostDetailView(generic.DetailView):
    model = Post

class AuthorListView(generic.ListView):
    model = CustomUser
    context_object_name = 'authors'
    template_name = 'blog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = CustomUser
    template_name = 'blog/author_list.html'
    context_object_name = 'author'

@login_required(login_url="/accounts/login")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save article to the database
            return redirect('blog:index')
    else:
        form = forms.CreatePost()
    return render(request, 'blog/post_create.html', { 'form': form })

