from django.shortcuts import render
from .models import Post, Category, PostCategory
from .forms.form_blog import PostForm
from django.shortcuts import redirect
from django.utils.text import slugify


def posts(request):
    posts = Post.objects.all()

    COLORS = {
        '1': 'text-bg-primary',
        '2': 'text-bg-secondary',
        '3': 'text-bg-success',
    }
    post_list = []
    for post in posts:
        categories = post.categories.all()
        cat_colors = {category.id: COLORS[str(category.color)] for category in categories}

        post_info = {
            'title': post.title,
            'create_at': post.create_at,
            'content': post.content,
            'categories': cat_colors
        }
        post_list.append(post_info)

    context = {
        'posts': post_list
    }
    return render(request, context=context, template_name='blog/posts.html')


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        categories = request.POST.getlist('categories')  # Obtener las categorías seleccionadas

        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.save()

            for category_id in categories:
                PostCategory.objects.create(post=new_post, category_id=category_id)

            return redirect('posts')

    else:
        post_form = PostForm()
        categories = Category.objects.all()

    return render(request, 'blog/post_form.html', {'post_form': post_form, 'categories': categories})