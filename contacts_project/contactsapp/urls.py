from django.conf.urls import url
from contactsapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^organization/(?P<org_slug>[\w\-]+)/$',
        views.show_org, name='show_org'),
    url(r'^organization/(?P<org_slug>[\w\-]+)/(?P<c_id>[\w\-]+)/$',
        views.show_con, name='show_con'),
]
