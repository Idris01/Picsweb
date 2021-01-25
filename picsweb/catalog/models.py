from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
 profile=models.ForeignKey("Profile", on_delete=models.SET_NULL, null=True)
 
 

class Profile(models.Model):
  picture = models.ImageField(upload_to="static/profile", null=True, blank=True)

class Upload(models.Model):
  picture =models.ImageField(upload_to="static/upload", null=False)
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  title=models.CharField(max_length=50, help_text="title of uploaded picture")
  description=models.CharField(max_length=200,help_text="short description of the picture", null=True)
  
  @property
  def upload_url(self):
    return self.picture.url
    
  def __str__(self):
    return self.title