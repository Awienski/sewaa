from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns =[
    path('', views.index, name='index'),
    path('blog_category/<category>/', views.blog_category, name='blog_category'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('commment/<int:id>/', views.comment, name='comment'),
    path('see_request/', views.see_request, name='see_request'),
    path('user_info/', views.user_info, name='user_info'),
    path('private_place/', views.private_place, name='private_place'),
    path('accounts/', include('django.contrib.auth.urls')),
]
