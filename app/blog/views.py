from django.shortcuts import render

# Create your views here.
import os
from django.views.generic import TemplateView
from django.http import Http404
from butter_cms import ButterCMS


class BlogListView(TemplateView):
    template_name = 'blog_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        client = ButterCMS(os.getenv('BUTTER_KEY'))

        response = client.posts.all()
        context['posts'] = response.get("data", None)

        return context


class BlogDetailView(TemplateView):
    template_name = "blog_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        client = ButterCMS(os.getenv('BUTTER_KEY'))

        try:
            response = client.posts.get(kwargs.get("slug"))
            context['post'] = response.get('data', None)
        except Exception:
            raise Http404("Post not found")
        return context
