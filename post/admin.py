from django.contrib import admin
from post.models import (Post,
                         Report)
# Register your models here.

admin.site.register(Post)
admin.site.register(Report)
