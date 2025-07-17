from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'main/home_page.html', {'posts': posts})


def created_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('HomePage')
    else:
        form = PostForm()
    return render(request, 'main/created_page.html', {'form': form})
