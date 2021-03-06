from django.conf.urls import url
from contactsapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^organizations/(?P<alphabet>[\w\-]+)/$',
        views.show_org_alpha, name='show_org_alpha'),
    url(r'^organizations/locale/(?P<nation>[\w\-]+)/$',
        views.show_org_nation, name='show_org_nation'),
    url(r'^organizations/', views.show_org_all, name='show_org_all'),
    url(r'^about/', views.about, name='about'),
    url(r'^addresses/role/(?P<role>[\w\-]+)/$',
        views.show_con_roles, name='show_con_roles'),
    url(r'^addresses/(?P<alphabet>[\w\-]+)/$',
        views.show_con_alpha, name='show_con_alpha'),
    url(r'^addresses/', views.show_con_all, name='show_con_all'),
    url(r'^new_org/$', views.add_org, name='add_org'),
    url(r'^new_con/$', views.add_con, name='add_con'),
    url(r'^edit_con/(?P<c_id>[\w\-]+)/$',
        views.edit_con, name='edit_con'),
    url(r'^edit_org/(?P<org_slug>[\w\-]+)/$',
        views.edit_org, name='edit_org'),
    url(r'^organization/(?P<org_slug>[\w\-]+)/$',
        views.show_org, name='show_org'),
    url(r'^con/(?P<c_id>[\w\-]+)/$',
        views.show_con, name='show_con'),
    url(r'^del_org/(?P<org_slug>[\w\-]+)/$',
        views.del_org, name='del_org'),
    url(r'^del_con/(?P<c_id>[\w\-]+)/$',
        views.del_con, name='del_con'),
    url(r'^search/', views.search, name='search'),
    url(r'^remove_pic/(?P<c_id>[\w\-]+)/$', views.remove_pic, name='remove_pic'),
    url(r'^remove_logo/(?P<org_slug>[\w\-]+)/$', views.remove_logo, name='remove_logo'),
]
