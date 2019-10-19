
from django.contrib import admin
from django.urls import path,re_path,include
from .views import (home_page,about_us,contact_us,example_page)
from django.views.generic.base import  RedirectView
from blog.views import ( blog_post_detail_page,blog_post_list_view,blog_post_create_view,blog_post_delete_view,blog_post_update_view,blog_post_retrieve_view)
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('blog-new/',blog_post_create_view),
    path('blog/',include('blog.urls')),
    path('',home_page),
    path('about',about_us),
    path('example',example_page),
    path('contact/',contact_us),
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', favicon_view),
]
