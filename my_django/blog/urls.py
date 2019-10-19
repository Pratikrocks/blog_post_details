from django.contrib import admin
from django.urls import path,re_path
from django.views.generic.base import  RedirectView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

#from my_django.views import (home_page,about_us,contact_us,example_page)
from blog.views import ( blog_post_detail_page,blog_post_list_view,blog_post_create_view,blog_post_delete_view,blog_post_update_view,blog_post_retrieve_view)
urlpatterns = [
    path('<int:id_post>/edit',blog_post_update_view),
    path('<int:id_post>/delete',blog_post_delete_view),

    #path('blog-new',blog_post_create_view),
    path('',blog_post_list_view),
    path('<int:id_post>/',blog_post_detail_page),
    re_path(r'^favicon\.ico$', favicon_view),

]
