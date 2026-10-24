from django.shortcuts import render, redirect
from .models import Blogs, Category, Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.
def posts_by_category(request, category_id):
  # Fetch the post that belongs to category with category_id
  posts = Blogs.objects.filter(status='published', category=category_id)
  try:
    category = Category.objects.get(pk=category_id)
  except:
    return redirect('home')
  # category = get_object_or_404(Category, pk=category_id)
  context = {
    'posts' : posts,
    'category' : category
  }
  return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
  single_post = get_object_or_404(Blogs, slug=slug, status='published')
  if request.method == "POST":
    comments = Comment()
    comments.user = request.user
    comments.blog = single_post
    comments.comment = request.POST['comment']
    comments.save()
    return HttpResponseRedirect(request.path_info)
  comments = Comment.objects.filter(blog = single_post)
  context = {
    'single_post' : single_post,
    'comments' : comments
  }
  return render(request, 'blogs.html', context)  

# Search Functionality
def search(request):
  keyword = request.GET.get('keyword')
  blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
  context = {
    'blogs' : blogs,
    'keyword' : keyword
  }
  return render(request, 'search.html', context)