from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import Entry, Tag, Category


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


class TagDetailView(generic.DetailView):
    template_name = 'blog/tag.html'
    model = Tag


class CategoryDetailView(generic.DetailView):
    template_name = 'blog/category.html'
    model = Category


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username,
                                password=raw_password)
            login(request, user)
            return redirect('blog:index')
    else:
        form = UserCreationForm()
        return render(request, 'blog/signup.html',
                      context={'form': form})
