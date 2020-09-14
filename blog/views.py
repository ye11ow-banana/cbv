from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Blog, Category


class MainPage(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'


class Blogs(ListView):
    model = Blog
    template_name = 'blog.html'


class Blog(DetailView):
    model = Blog
    slug_field = 'url'
    template_name = 'single-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Blog.objects.all().order_by('-pub_date')
        return context
