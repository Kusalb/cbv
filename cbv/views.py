from django.shortcuts import render
from django.views.generic import TemplateView

from cbv.models import Post
# Create your views here.

class Ex2View(TemplateView):
    template_name = "ex2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.get(id=1)
        context["data"] = "context data for Ex2"
        return context