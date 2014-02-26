from django.contrib import admin
from myblog.models import Post
from myblog.models import Category
from django.db import models

admin.site.register(Post)
admin.site.register(Category)
