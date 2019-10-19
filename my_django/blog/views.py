from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.admin.views.decorators import  staff_member_required
from django.http import Http404

# Create your views here.

from my_django.forms import ContactForm,BlogPostForm
from .models import BlogPost
#obj=BlogPost.objects.get(id=1)


def blog_post_detail_page(request,id_post):
    print("Django says",request.method,request.user)
    try:
        qs=BlogPost.objects.filter(id=id_post)
        obj=qs[0]
    except:
        raise Http404
    template_name='blog/blog_post_detail.html'
    context={"object":obj}
    return render(request,template_name,context)

#GET-> retrieve/ List
#post-> create/ update/ delete
#create retrive update delete

def blog_post_list_view(request):
    qs=BlogPost.objects.all()

    template_name='blog/blog_post_list.html'
    context={'object_list':qs}

    return render(request,template_name,context)


def blog_post_retrieve_view(request):
    template_name = 'blog/blog_post_list.html'
    context = {'object_list': []}

    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request,id_post):
    obj = get_object_or_404(BlogPost,id=id_post)
    for content in request:
        print(content)
    form = BlogPostForm(request.GET,instance=obj)

    if form.is_valid():
        form.save()

    template_name = 'form.html'
    context = {'form': form,"title":f"Update { obj.title }"}

    return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
    form = BlogPostForm(request.POST or None)

    print(form.is_valid())
    if form.is_valid():
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get("title")
        obj.save()
        form = BlogPostForm()
    template_name = 'blog/blog_post_create.html'
    context = {'form': form}

    return render(request, template_name, context)


def blog_post_delete_view(request,id_post):
    obj=get_object_or_404(BlogPost,id=id_post)
    print(request.method)
    if request.method=="GET":
        obj.delete()

        return redirect('/blog')
    template_name = 'blog/blog_post_delete.html'
    context = {'object_list': obj}

    return render(request, template_name, context)


