from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Designer.objects
    blist = Designer.objects.all()
    paginator = Paginator(blist, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def introduce(request):
    return render(request, 'introduce.html')
  
def update(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id)
    else:
        return render(request, 'update.html', {'designer' : post})
        
def create(request):
    if request.method == 'POST':
        designer = Designer()
        designer.image = request.FILES['p']
        designer.name = request.POST['n']
        designer.address = request.POST['a']
        designer.description = request.POST['d']
        designer.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def delete (request, pk):
    blog = get_object_or_404(Designer, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, pk):
    detail = get_object_or_404(Designer, pk=pk)
    return render(request, 'detail.html', {'detail':detail})