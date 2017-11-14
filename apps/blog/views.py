from django.shortcuts import render
from django.views import generic

from .models import Entry


class EntryListView(generic.ListView):
    model = Entry
    paginate_by = 4
    context_object_name = 'entry_list'


class IndexView(EntryListView):
    template_name = 'blog/index.html'


class EntryDetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Entry


class SearchEntryView(EntryListView):
    template_name = 'blog/search.html'

    def get_queryset(self):
        query = self.request.GET.get('input')
        result = Entry.search_entry(query)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('input')
        return context
