
from django.urls import path,re_path
from . import views

app_name = 'blog'
#第一种方法path
urlpatterns = [
    path('index/', views.index),
    path('article/<int:article_id>/', views.article_page,name='article_page'),
    path('edit/<int:article_id>/', views.edit_page,name='edit_page'),
    path('edit_action/', views.edit_action,name='edit_action')
]

#第二种方法re_path
# urlpatterns = [
#     re_path('index/', views.index),
#     re_path('article/(?P<article_id>[0-9]+)/', views.article_page),
# ]

# urlpatterns = [
#     path('index/',views.index),
#     re_path('article/(?P<article_id>[0-9]+)/', views.article_page), #使用正则表达式配置路由
# ]
