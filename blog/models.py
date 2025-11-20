from django.db import models
from django.contrib.auth.models import User

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
    




class Comment(models.Model):
    roll=models.AutoField(primary_key=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username}"
