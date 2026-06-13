from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Authorization: only the author can edit
    if post.user != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'users/edit_post.html', {'form': form, 'post': post})