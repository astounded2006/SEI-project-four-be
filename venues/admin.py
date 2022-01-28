from django.contrib import admin
from .models import Venue, Comment, Like
# Register your models here.
admin.site.register(Venue)
admin.site.register(Comment)
admin.site.register(Like)
