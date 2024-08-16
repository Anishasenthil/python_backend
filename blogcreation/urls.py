from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views    #added 

from .views import view_blog

urlpatterns = [
    path('base/',views.base,name="base"),
    path('bloglist/',views.bloglist,name="bloglist"),
    path('create_blog/',views.create_blog,name="create_blog"),
    path('login/', auth_views.LoginView.as_view(), name='login'),  #added
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),     #added

    path('blog/<int:blog_id>/', view_blog, name='view_blog'),  #added
]