"""classblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:   path('blog/', include('blog.urls'))
User auth:
accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='index'),
    path('blog/', views.BlogListView.as_view(),name='blog-list'),
    path('blog/<int:pk>',views.blog_detail,name='blog-detail'),
    #path('author/', views.author,name='author'),
    path('accounts/',include('django.contrib.auth.urls')),
    # (?P<post_id>\d+)
    path('blog/<int:pk>/share/', views.post_share,name='post_share'),
]
