from distutils.command import upload
from django.db import models
import django.utils.timezone
import django.db.models
# Create your models here.
a ='General'
b ='Mathematics'
c ='Science'
d ='Socialscience'
e ='Commerce'
f ='Computer'
g ='Coding'
h ='English'
i ='Hindi'
j ='Sports'
k ='Health'
l ='Food'
m ='Entertainment'
n ='Other'
class Blog(models.Model):
    blog_title = models.CharField(max_length=500,default='Title')
    description = models.CharField(max_length=2000,default='description')

    blog_para1 = models.CharField(max_length=1000000,default='Para1')
    blog_para2 = models.CharField(max_length=100000,default='Para2')
    blog_para3 = models.CharField(max_length=100000,default='Para3')
    blog_para4 = models.CharField(max_length=1000000,default='Para4')

    blog_para1_heading = models.CharField(max_length=10000,default='')
    blog_para2_heading = models.CharField(max_length=10000,default='')
    blog_para3_heading = models.CharField(max_length=10000,default='')
    blog_para4_heading = models.CharField(max_length=10000,default='')

    image = models.FileField(upload_to='', default='imgTOP')
    middleimage = models.FileField(upload_to='', default='imgMIDDLE')
    bottomimage = models.FileField(upload_to='', default='imgBOTTOM')

    category = models.CharField(max_length=100,default='General', choices=[(a,a),(b,b),(c,c),(d,d),(e,e),(f,f),(g,g),(h,h),(i,i),(j,j),(k,k),(l,l),(m,m),(n,n)])
    creator = models.CharField(max_length=100,default='AUTHOR')
    user = models.CharField(max_length=1000,default='')
    published_date = models.DateField(default=  django.utils.timezone.now)

    def __str__(self):
        return self.blog_title

class feedback(models.Model):
    feedbacker = models.CharField(max_length=30, default='DEFAULT')
    feedbacker_userid = models.CharField(max_length=30, default='DEFAULT')
    feedbacker_email = models.EmailField(max_length=100,default='none@gmail.com')
    feedback = models.CharField(max_length=600,default='NO FEEDBACK')
    published_date = models.DateField(default= django.utils.timezone.now)

    def __str__(self):
        return self.feedbacker_email