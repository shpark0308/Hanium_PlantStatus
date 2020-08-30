from . import views
from django.urls import path
from django.conf.urls import url

app_name="plantism"
urlpatterns = [
    path('', views.index, name='index'),
    #path('codeform', views.codeform, name="codeform"),
    #path('pro', views.pro ,name="pro"),
    #path('compare', views.compare,name="compare"),
    #path('postcreate/', views.postcreate, name='postcreate'),
    path('detail1/<int:number>/', views.detail1, name='detail1'),
    #url(r'^detail1/(?P<number>[0-9]+)/$', views.detail1, name='detail1'),
]
