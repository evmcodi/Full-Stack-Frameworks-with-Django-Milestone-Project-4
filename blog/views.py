from django.shortcuts import render, redirect, reverse

# Create your views here.
from blog.forms import BlogForm
from blog.models import Blog


def view_blog(request):
    """ A view that renders the bag contents page """

    # Retrieve the blog posts starting with latest blog.
    blogs = Blog.objects.all().reverse()

    context = {
        'blogs': blogs
    }

    return render(request, 'blog/blog.html', context)


def create_blog(request):

    user = request.user

    # Check if the logged in user has 'Publisher' permission.
    if user.has_perm('blog.publish_blog_posts'):
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = BlogForm()

        return render(request, 'blog/create-blog.html', {'form': form})

    # If user doesn't have 'Publish' permission - redirect to blog list view.
    return redirect(reverse('view_blog'))
