from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippets_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]