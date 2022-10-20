from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
class Flier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='dp_fliers', default='r.jpg')
    imageString  = models.TextField()
    htmlFile  = models.TextField(blank=True,null=True)
    no_of_clicks  = models.IntegerField(default=0)
    hashtag1  = models.CharField(max_length=100,blank=True,null=True)
    hashtag2  = models.CharField(max_length=100,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.event_name
    
