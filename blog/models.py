from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from pickle import TRUE
# Create your models here.
class post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    content=models.TextField()

    def __str__(self):
        return "posted by " + self.author + " on " + self.title
    


class BlogComments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey('post',on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=TRUE)
    timestamp=models.DateTimeField(default=now)