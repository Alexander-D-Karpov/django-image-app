from django.contrib import admin

# Register your models here.
from pics.models import Image, Group, ImageInGroup

admin.site.register(Image)
admin.site.register(Group)
