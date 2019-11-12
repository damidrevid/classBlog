from django.urls import path
from . import views # The dot (.) indicate the current directory.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #Django automatically assign a primary key PK for every post even though we didn't indicate this while creating our model.
                                                                   #Now we go to Views to create post.detail
]