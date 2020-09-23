from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_reported = models.DateField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField("Post Image", upload_to='uploads/')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(settings.)

    class Meta:
        ordering = ['-updated']

    def get_summary(self):
        return self.content[:20] + '...'

    def __str__(self):
        return self.title
