from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CategoryForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_delete
from django.dispatch import receiver


def home_page(request):
    '''
    Домашняя страница с выводом всех постов.

    GET:
    - Отображает список постов.
    - Фильтрация по категории через CategoryForm.

    Returns:
        HTML страницу с постами и формой фильтрации.
    ''' 
    posts = Post.objects.all()
    if request.method == 'GET':
        form = CategoryForm(request.GET)
        if form.is_valid():
            category_id = form.cleaned_data['category']
            if category_id:
                posts = posts.filter(category__id=category_id)
    return render(request,
                  'main/home_page.html', {'posts': posts, 'form': form})


@login_required
def create_post(request):
    '''
    Создание нового поста (только для авторизованных пользователей).

    POST:
        - Обрабатывает PostForm.
        - Присваивает авторство текущему пользователю.
        - Сохраняет пост и перенаправляет на главную.

    GET:
        - Отображает пустую форму для создания поста.
    '''
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
    '''
    Редактирование поста (только автором).

    POST:
        - Обновляет данные поста через PostForm.
        - Перенаправляет на главную.

    GET:
        - Отображает форму с текущими данными поста.
    '''
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
    else:
        form = PostForm(instance=post)
    return render(request, 'main/edit_page.html', {'post': post, 'form': form})


@login_required
def delete_post(request, id):
    '''
    Удаление поста (только автором).

    POST:
        - Удаляет пост и перенаправляет на главную.
    '''
    post = get_object_or_404(Post, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('HomePage')


def detail_post(request, id):
    '''
    Детальная страница поста с комментариями.

    GET:
        - Отображает детали поста и список комментариев.
        - Отображает форму добавления комментария.

    POST:
        - Сохраняет новый комментарий текущего пользователя.
    '''
    post = get_object_or_404(Post, id=id)
    comm = Comment.objects.filter(post=post)

    if request.method == 'POST':
        comments = CommentForm(request.POST, request.FILES)
        if comments.is_valid():
            comment = comments.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    else:
        comments = CommentForm()

    return render(request,
                  'main/detail_page.html',
                  {'post': post, 'comments': comments, 'comm': comm})


@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    '''
    Сигнал: при удалении поста автоматически удаляет файл изображения с диска.
    '''
    if instance.image:
        instance.image.delete(False)
