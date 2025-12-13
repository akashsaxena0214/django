from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.db.models import Q

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q')
    cat = request.GET.get('category')
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
    if cat:
        qs = qs.filter(category__slug=cat)
    paginator = Paginator(qs, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'q': q})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post.get_absolute_url())
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect(post.get_absolute_url())
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('post_list')
    return render(request, 'registration/register.html', {'form': form})

@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(post.get_absolute_url())
