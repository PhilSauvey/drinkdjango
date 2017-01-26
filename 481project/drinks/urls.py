from django.conf.urls import url

from . import views

app_name='drinks'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<drink_slug>[A-Za-z0-9_]+)/$', views.detail,name='detail'),
	url('search', views.search, name='search'),
	url('results',views.results, name='results'),
	url('mydrinks',views.mydrinks, name='mydrinks'),
	url('newuser',views.createUser, name='newuser'),
	url('populate',views.populate,name="populate"),
]

