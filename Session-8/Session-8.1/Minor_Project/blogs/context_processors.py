from .models import Category

def getCategories(request):
  categories = Category.objects.all()
  return dict(categories=categories)