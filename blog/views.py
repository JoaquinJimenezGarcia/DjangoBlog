from django.shortcuts import render
from django.utils import timezone
from .models import BlogPost

# Create your views here.
def post_list(request):
    posts = BlogPost.objects.filter(timestamp__lte=timezone.now()).order_by('timestamp')
    print(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})