# Create your views here.
from django.shortcuts import render_to_response
from blog.models import post

def home(request):
    entries = post.objects.all()[:10]
#    content = {
#        'title' : 'My First Post',
#        'author' : 'Thung Han',
#        'date' : '28th January 2013',
#        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus tempus dui, ut vulputate nisl eleifend eget. Aenean justo felis, dapibus quis vulputate at, porta et dolor. Praesent enim libero, malesuada nec vestibulum vitae, fermentum nec ligula. Etiam eget convallis turpis. Donec non sem justo.',
#    }
#    return render_to_response('index.html', content)
    return render_to_response('index.html', {'post' : entries})