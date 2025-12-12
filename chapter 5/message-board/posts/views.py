from django.views.generic import ListView # new
from .models import Post
class PostList(ListView): # new
    model = Post
template_name = "post_list.html"    