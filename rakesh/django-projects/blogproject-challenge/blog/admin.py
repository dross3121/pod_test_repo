from django.contrib import admin
from .models import Comments, Tag, Post
# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comments)