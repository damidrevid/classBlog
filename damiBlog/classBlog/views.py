from django.shortcuts import render, get_object_or_404 #We imported 'get_object_or_404' to control what's displayed when onbect is not available
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'classBlog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'classBlog/post_detail.html', {'reveal':post})