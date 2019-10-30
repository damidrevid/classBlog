from django.contrib import admin

#In order to make the table created to show in our admin.py (You do this for every table)
from .models import Post

# Register your models here.
# This is to make the table 
admin.site.register(Post)