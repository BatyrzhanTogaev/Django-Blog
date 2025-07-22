from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CategoryForm
from .models import Post
from django.contrib.auth.decorators import login_required


def home_page(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        form = CategoryForm(request.GET)
        if form.is_valid():
            category_id = form.cleaned_data['category']
            if category_id:
                posts = posts.filter(category__id=category_id)
    return render(request, 'main/home_page.html',
                  {'posts': posts, 'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('HomePage')
    else:
        form = PostForm()
    return render(request, 'main/create_page.html', {'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
    else:
        form = PostForm()
    return render(request, 'main/edit_page.html', {'post': post, 'form': form})


@login_required
def delete_post(request, id,):
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('HomePage')


def detail_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'main/detail_page.html', {'post': post})
