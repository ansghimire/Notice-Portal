from django.contrib import admin

# Register your models here.
from . models import Notice, Advertisement, Category

admin.site.register(Notice)
admin.site.register(Advertisement)
admin.site.register(Category)