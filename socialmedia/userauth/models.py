from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True, default='')
    

    def __str__(self):
        return self.user.username

class Post(models.Model):
    STATUS = [("DENIED", "DENIED"), ("ALLOWED", "ALLOWED"), ("PENDING", "PENDING")]
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    status = models.CharField(default=STATUS[2][0], choices=STATUS, max_length=10)
    talent = models.BooleanField(default=False)

    def update(self):
        self.updated_at = datetime.now()
        self.save()
    def __str__(self):
        return f"{self.user}-{self.id}"

class PostRatings(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    ratings = models.IntegerField(default=0, choices=[(i, i) for i in range(0, 3)])

    def __str__(self):
        return f"{self.username}-{self.post_id}"

class TalentOfTheMonth(models.Model):
    user = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.month}/{self.year}"


class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

    
    
