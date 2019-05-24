from django.conf.urls import url,include
from blog import views

app_name= 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
]
