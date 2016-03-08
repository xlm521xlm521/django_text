from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns( '',
        url(r'^$', views.index, name='index' ) ,
        url(r'^showpython/', views.showpython, name='showpython'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # New!
        url( r'^add_category/$' , views.add_category, name='add_category' ) , # NEW MAPPING!   
)
