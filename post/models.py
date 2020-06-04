from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_summary(self):
        return self.content[:10] + '...'

    def __str__(self):
        return self.title
