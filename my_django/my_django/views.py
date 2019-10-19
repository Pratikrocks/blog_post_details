from django.http import HttpResponse
from django.shortcuts import   render
from django.template.loader import get_template
from django import forms
from .forms import  ContactForm

def home_page(request):
    title="Hello there..."
    context={"title":title}
    template_name="title.txt"
    template_obj=get_template(template_name)
    rendered_item=template_obj.render(context)
    return render(request,template_name,{"title":rendered_item})

def contact_us(request):
    form=ContactForm(data=request.POST or None)

    if form.is_valid():

        print(form.cleaned_data)
        form=ContactForm()

    return render(request,"form.html",{"title":'Contact Us',"form":form})

def about_us(request):
    return HttpResponse("<h1>About Us</h1>")

def example_page(request):
    context={"title":"Example"}
    template_name="hello_world.html"
    template_obj=get_template(template_name)
    return HttpResponse(template_obj.render(context))