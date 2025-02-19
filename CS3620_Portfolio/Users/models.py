from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    # linkedin_url = models.URLField(max_length=400, null=True, blank=True)
    # github_url = models.URLField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.user.username