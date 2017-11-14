from django.test import TestCase

from .utils import create_entry
from ..models import Entry


class EntryModelTestCase(TestCase):

    def setUp(self):
        self.entry = create_entry(name="Test entry",
                                  category_name="Test",
                                  text="Text Text",)
        self.entry.tag_set.create(name='Awesome')
        self.entry2 = create_entry(name='Past entry',
                                   category_name="Time",
                                   text='Here we are',
                                   days_from_now=-100)
        self.entry3 = create_entry(name='Future entry',
                                   category_name='Time',
                                   text='Man this thing is serious',
                                   days_from_now=100)

    def __test_search_entry(self, input, entries_expected):
        results = Entry.search_entry(input)
        self.assertQuerysetEqual(results, entries_expected)

    def test_search_entry_with_random_input(self):
        self.__test_search_entry('asdfasdfa', [])

    def test_search_entry_with_title(self):
        self.__test_search_entry('past', ['<Entry: Past entry>'])

    def test_search_entry_with_tag(self):
        self.__test_search_entry('awesome', ['<Entry: Test entry>'])

    def test_search_entry_with_category(self):
        self.__test_search_entry(
            'time', ['<Entry: Future entry>', '<Entry: Past entry>']
        )

    def test_search_entry_order_by_pub_date(self):
        self.__test_search_entry(
            'entry', ['<Entry: Future entry>',
                      '<Entry: Test entry>',
                      '<Entry: Past entry>',]
        )
