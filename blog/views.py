from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def view_blog(request):
    """ A view that renders the bag contents page """

    # Retrieve only the current user's terms.
    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs
    }

    return render(request, 'blog/blog.html', context)
