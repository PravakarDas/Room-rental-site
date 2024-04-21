from django.db import models

# Create your models here.

class Register(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=100) 
    nid=models.IntegerField() 

class Comment(models.Model):
    comment = models.TextField(null = True)
    commented_by = models.ForeignKey(Register, on_delete=models.CASCADE)

class DormRoom(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    popularity = models.IntegerField(default=0)
    type = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    link = models.URLField(max_length=200, null=True)
    posted_by = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='posted')
    comments = models.ManyToManyField(Comment, blank=True)
    bookmarked_by = models.ManyToManyField(Register, blank=True, related_name='bookmarked')

class Notification(models.Model):
    post = models.ForeignKey(DormRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(Register, on_delete=models.CASCADE)

class Discussion(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)