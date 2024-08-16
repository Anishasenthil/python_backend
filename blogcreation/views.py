from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import BlogPost
from . forms import BlogPostForm

from django.shortcuts import render, get_object_or_404  #added
from .models import BlogPost


 
# Create your views here.
def base(request):
    return HttpResponse("Hello world")

def bloglist(request):
    blogs=BlogPost.objects.all
    return render(request,'bloglist.html',{'blogs':blogs})

def create_blog(request):
    if request.method == 'POST':
        form=BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bloglist')
    else:
        form=BlogPostForm()
    return render(request,'create_blog.html',{'form':form})




def view_blog(request, blog_id):                   #added
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'view_blog.html', {'blog': blog})
