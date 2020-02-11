from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # auto_now = True --> this updates the date everytime the post is updated...
    # auto_now_add = True --> it puts the current date when the post was created. But it doesn't allows to change the date
    author = models.ForeignKey(User, on_delete = models.CASCADE)    # if user is deleted, delete their post also

    def __str__(self):
        '''this method is used for testing purposes only...'''
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


