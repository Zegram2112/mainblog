from django.conf.urls import url
from .views import IndexView, EntryDetailView, SearchEntryView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(),
        name='index'),
    url(r'^(?P<pk>[0-9]+)/$', EntryDetailView.as_view(),
        name='detail'),
    url(r'^search/$', SearchEntryView.as_view(),
        name='search'),
]