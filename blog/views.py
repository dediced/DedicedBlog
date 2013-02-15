from django.shortcuts import render_to_response
from blog.models import Post

def home(request):
    post_list = Post.objects.all().order_by('-timestamp')[:10]
    return render_to_response('posts.html', {'post' : post_list})
