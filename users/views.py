from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.select_related('user').order_by('-created_at')
    return render(request, 'users/home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request,'users/create_post.html',{'form':form})