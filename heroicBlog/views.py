from turtle import title
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
import datetime
from .models import Blog, feedback,a,b,c,d,e,f,g,h,i,j,k,l,m,n
import os

# Cleaning media

def cleanMedia():
    usedImages = []
    images = os.listdir('./media')
    for i in range(0,len(images)):
        usedImages.append(images[i])
        images1 = Blog.objects.filter(image= images[i])
        images2 = Blog.objects.filter(middleimage= images[i])
        images3 = Blog.objects.filter(bottomimage= images[i])
        for j in images1:
            usedImages.remove(j.image)
        for k in images2:
            usedImages.remove(k.middleimage)
        for l in images3:
            usedImages.remove(l.bottomimage)
    for m in range(0,len(usedImages)):
        os.remove(f'./media/{usedImages[m]}')


# Blog Categories
blogCategories = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
# DRY
def getBlogs(request,isMyBlog):
    if(isMyBlog):
        title = "My Blogs"
        current_user = request.user
        allBlogs = Blog.objects.filter(user=current_user)
        generalBlogs = Blog.objects.filter(category=a,user=current_user)
        mathematicsBlogs = Blog.objects.filter(category=b,user=current_user)
        scienceBlogs = Blog.objects.filter(category=c,user=current_user)
        socialscienceBlogs = Blog.objects.filter(category=d,user=current_user)
        commerceBlogs = Blog.objects.filter(category=e,user=current_user)
        computerBlogs = Blog.objects.filter(category=f,user=current_user)
        codingBlogs = Blog.objects.filter(category=g,user=current_user)
        englishBlogs = Blog.objects.filter(category=h,user=current_user)
        hindiBlogs = Blog.objects.filter(category=i,user=current_user)
        sportsBlogs = Blog.objects.filter(category=j,user=current_user)
        healthBlogs = Blog.objects.filter(category=k,user=current_user)
        foodBlogs = Blog.objects.filter(category=l,user=current_user)
        entertainmentBlogs = Blog.objects.filter(category=m,user=current_user)
        otherBlogs = Blog.objects.filter(category=n,user=current_user)
    else:
        title = "Home"
        allBlogs = Blog.objects.all()
        generalBlogs = Blog.objects.filter(category=a)
        mathematicsBlogs = Blog.objects.filter(category=b)
        scienceBlogs = Blog.objects.filter(category=c)
        socialscienceBlogs = Blog.objects.filter(category=d)
        commerceBlogs = Blog.objects.filter(category=e)
        computerBlogs = Blog.objects.filter(category=f)
        codingBlogs = Blog.objects.filter(category=g)
        englishBlogs = Blog.objects.filter(category=h)
        hindiBlogs = Blog.objects.filter(category=i)
        sportsBlogs = Blog.objects.filter(category=j)
        healthBlogs = Blog.objects.filter(category=k)
        foodBlogs = Blog.objects.filter(category=l)
        entertainmentBlogs = Blog.objects.filter(category=m)
        otherBlogs = Blog.objects.filter(category=n)

    params = {
        'allBlogs' : allBlogs,
        'generalBlogs': generalBlogs,
        'mathematicsBlogs': mathematicsBlogs,
        'scienceBlogs': scienceBlogs,
        'socialscienceBlogs': socialscienceBlogs,
        'commerceBlogs': commerceBlogs,
        'computerBlogs': computerBlogs,
        'codingBlogs': codingBlogs,
        'englishBlogs': englishBlogs,
        'hindiBlogs': hindiBlogs,
        'sportsBlogs': sportsBlogs,
        'healthBlogs': healthBlogs,
        'foodBlogs': foodBlogs,
        'entertainmentBlogs': entertainmentBlogs,
        'otherBlogs': otherBlogs,
        "blogCategories" : blogCategories,
        "myBlog" : isMyBlog,
        "title": title
    }
    return params

# Create your views here.
def index(request):
    return render(request,'index.html', getBlogs(request,False) )

def showBlog(request):
    blog_title_ = str(request.GET.get('blog_id', 'default'))
    description_ = str(request.GET.get('blog_des','default'))
    creator_ = str(request.GET.get('blog_creator', 'default'))
    user_ = str(request.GET.get('user', 'default'))
    currentBlog = Blog.objects.filter(blog_title=blog_title_, description=description_, creator=creator_, user=user_)
    params = {
        "blogs" : currentBlog
    }
    return render(request,'showblog.html',params)

def aboutus(request):
    return render(request,'aboutus.html')

def creatingBlog(request):
    return render(request,'createblog.html')


def createBlog(request):

    blog = Blog()
    image = request.FILES.get('mainImage', '')
    middleimage = request.FILES.get('subImage1', '')
    bottomimage = request.FILES.get('subImage2', '')

    blog.blog_title = request.POST.get('blogTitle', 'default')
    blog.description = request.POST.get('description', 'default')

    blog.blog_para1  = request.POST.get('para1', '')
    blog.blog_para2  = request.POST.get('para2', '')
    blog.blog_para3  = request.POST.get('para3', '')
    blog.blog_para4  = request.POST.get('para4', '')

    blog.blog_para1_heading = request.POST.get('headingPara1','')
    blog.blog_para2_heading = request.POST.get('headingPara2','')
    blog.blog_para3_heading = request.POST.get('headingPara3','')
    blog.blog_para4_heading = request.POST.get('headingPara4','')

    blog.image = image
    blog.middleimage = middleimage
    blog.bottomimage = bottomimage
    blog.category = request.POST.get('categories', a)
    blog.creator = request.POST.get('creator', f'{request.user}')
    blog.user = request.user
    des = request.POST.get('description', 'default')
    title = request.POST.get('blogTitle', 'default')
    category = request.POST.get('categories', a)
    try:
        Blog.objects.get(description = des,blog_title = title ,category=category)
        params = {
            "text" : "Blog already exists"
        }
        return render(request,'404.html',params)
    except:
        blog.save()
        return HttpResponseRedirect('/')

def myblogs(request):
    return render(request,'index.html', getBlogs(request,True))

def deletingBlog(request):
    return render(request,'deleteBlog.html',getBlogs(request,True))

def deleteBlog(request):
    checks = request.GET.getlist('checks[]')
    for i in range(0,len(checks)):
        Blog.objects.filter(description= checks[i],user=request.user).delete()
    return HttpResponseRedirect('/myblogs')

# Login/Signin
signed_users = []

def showSignIn(request):
    return render(request,'2_signup.html')

def showLogIn(request):
    return render(request,'2_login.html')

def userFeedback(request):
    feedbacker_name = request.GET.get('feedback_name', 'default')
    feedbacker_email = request.GET.get('feedback_email', 'default')
    feedbacker_message = request.GET.get('feedback_message', 'default')
    Current_user = request.user

    _feedback = feedback()
    _feedback.feedbacker = feedbacker_name
    _feedback.feedbacker_email = feedbacker_email
    _feedback.feedback = feedbacker_message
    _feedback.feedbacker_userid = Current_user
    _feedback.save()
    return HttpResponseRedirect('/')


def signIn(request):
    user_name = request.GET.get('name','default')
    user_email = request.GET.get('email','default')
    user_password = request.GET.get('password','default')

    # Checking data

    if len(user_name) > 100 or len(user_email) < 4 or user_password == '':
        params = {
            "text" : "Very short email or password \n or Too long name."
        }
        return render(request,'404.html',params)

    signed_users.append(f'{user_email}')
    date = datetime.datetime.now()
    # Creating user
    myuser = User.objects.create_user(user_name,user_email,user_password)
    myuser.last_name = user_name
    myuser.save()
    return HttpResponseRedirect("/")

def logIn(request):

    login_name = request.GET.get('login_name')
    login_password = request.GET.get('login_password')
    user = authenticate( username= login_name, password= login_password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        params = {
        "text" : "Email or Password is wrong.Please try again"
        }
        return render(request,'404.html',params)