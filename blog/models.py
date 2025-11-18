from django.db import models

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