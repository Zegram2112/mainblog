from django.conf.urls import url
from . import views as v

app_name = 'blog'
urlpatterns = [
    url(r'^$', v.IndexView.as_view(),
        name='index'),
    url(r'^(?P<pk>[0-9]+)/$', v.EntryDetailView.as_view(),
        name='detail'),
    url(r'^search/$', v.SearchEntryView.as_view(),
        name='search'),
    url(r'^tag/(?P<pk>[0-9]+)/$', v.TagDetailView.as_view(),
        name='tag'),
    url(r'^category/(?P<pk>[0-9]+)/$', v.CategoryDetailView.as_view(),
        name='category')
]
