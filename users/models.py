from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('agent', 'agent'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures')
    user_type = models.CharField(max_length=10, choices=USER_CHOICES, default='buyer')
    user_bio = models.TextField(max_length=500, null=True, blank=True)
    contact_number = models.IntegerField(default=0, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    twitter_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'