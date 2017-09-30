from django.conf.urls import include, url
from . import views

urlpatterns =[
    url(r'^$',views.listar_publicacion),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='post_detail'),
    url(r'^post/nueva/$', views.nueva_publicacion,name='nueva_publicacion'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]
