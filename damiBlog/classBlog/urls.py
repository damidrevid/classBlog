from django.urls import path
from . import views # The dot (.) indicate the current directory.

urlpatterns = [
    path('', views.post_list, name='post_list'),
]