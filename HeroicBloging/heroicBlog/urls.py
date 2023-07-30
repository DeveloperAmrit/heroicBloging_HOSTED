from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path('about',views.aboutus,name='shopAboutUs'),
    path('createBlog',views.createBlog,name='createBlog'),
    path('creatingBlog',views.creatingBlog,name='createBlog'),
    path('myblogs',views.myblogs,name='myblogs'),
    path('showBlog',views.showBlog,name='showBlog'),
    path('deletingBlog',views.deletingBlog,name='deletingBlog'),
    path('deleteBlogs',views.deleteBlog,name='deletingBlog'),

    path('signing', views.showSignIn , name='signing'),
    path('logging', views.showLogIn, name='logging'),

    path('signin', views.signIn , name='signin'),
    path('login', views.logIn , name='signin'),

    path('feedback',views.userFeedback,name='feedback')
] 
