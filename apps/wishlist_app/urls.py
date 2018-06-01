from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^add_item$', views.add_item),
    url(r'^leave_item/(?P<item_id>\d+)', views.leave_item),
    url(r'^join_item/(?P<item_id>\d+)', views.join_item),
    url(r'^info/(?P<item_id>\d+)', views.info),
    url(r'^delete/(?P<item_id>\d+)', views.delete)

]
