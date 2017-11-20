from django.test import TestCase
from django.shortcuts import reverse

from . import utils
from ..views import Tag, Category


class IndexViewTestCase(TestCase):

    def test_empty_entry_list_show_notfound_message(self):
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['entry_list'], [])
        self.assertContains(response, 'There are no entries yet')

    def test_entry_list_show_entries(self):
        e = utils.create_entry()
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['entry_list'],
                                 ['<Entry: Entry>'])
        self.assertContains(response, "Entry")

    def test_entry_list_order_by_date(self):
        past_entry = utils.create_entry(name="Past Entry", days_from_now=-1)
        present_entry = utils.create_entry(name="Present Entry")
        future_entry = utils.create_entry(name="Future Entry", days_from_now=1)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['entry_list'],
                                 ['<Entry: Future Entry>',
                                  '<Entry: Present Entry>',
                                  '<Entry: Past Entry>'])


class EntryDetailViewTestCase(TestCase):

    def test_with_null_entry(self):
        response = self.client.get(reverse('blog:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_with_entry(self):
        entry = utils.create_entry()
        response = self.client.get(reverse('blog:detail', args=(entry.id,)))
        self.assertEqual(response.context['entry'], entry)


class SearchEntryViewTestCase(TestCase):

    def setUp(self):
        utils.create_entry(name="Past Entry", days_from_now=-30)
        utils.create_entry(name="Future Entry", days_from_now=30)

    def test_without_entry(self):
        response = self.client.get(reverse('blog:search'),
                                   data={'input': 'adsfasdf'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['entry_list'], [])

    def test_with_entries(self):
        # More in detail search tests are in test_models.EntryModelTestCase
        response = self.client.get(reverse('blog:search'),
                                   data={'input': 'Past'})
        self.assertQuerysetEqual(response.context['entry_list'],
                                 ['<Entry: Past Entry>'])
        self.assertContains(response, "Past")

    def test_order_by_pub_date(self):
        response = self.client.get(reverse('blog:search'),
                                   data={'input': 'Entry'})
        self.assertQuerysetEqual(response.context['entry_list'],
                                 ['<Entry: Future Entry>',
                                  '<Entry: Past Entry>',])

    def test_shows_input(self):
        response = self.client.get(reverse('blog:search'),
                                   data={'input': 'Hey man'})
        self.assertContains(response, 'Hey man')


class TagDetailTestCase(TestCase):

    def setUp(self):
        self.e1 = utils.create_entry(name='Entry Past',
                                     days_from_now=-30,
                                     tags=['time', 'past'])
        self.e2 = utils.create_entry(name='Entry Future',
                                     days_from_now=30,
                                     tags=['time', 'future'])
        self.time = Tag.objects.get(name='time')
        self.test = Tag.objects.create(name='test')

    def test_with_null_tag(self):
        response = self.client.get(reverse('blog:tag', args=(12342,)))
        self.assertEqual(response.status_code, 404)

    def test_with_correct_tag(self):
        response = self.client.get(reverse('blog:tag', args=(self.time.pk,)))
        self.assertContains(response, 'time')
        self.assertQuerysetEqual(
            response.context['tag'].entries.all(),[
                '<Entry: Entry Future>',
                '<Entry: Entry Past>',
        ])

    def test_tag_without_entries(self):
        response = self.client.get(reverse('blog:tag', args=(self.test.pk,)))
        self.assertContains(response, 'test')
        self.assertQuerysetEqual(response.context['tag'].entries.all(),
                                 [])


class CategoryDetailTestCase(TestCase):

    def setUp(self):
        self.e1 = utils.create_entry(name='Entry Past',
                                     days_from_now=-30,
                                     category_name='Time')
        self.e2 = utils.create_entry(name='Entry Future',
                                     days_from_now=30,
                                     category_name='Time')
        self.category = Category.objects.get(name='Time')
        self.empty_category = Category.objects.create(name='Empty')

    def test_with_inexistent_category(self):
        response = self.client.get(reverse('blog:category',
                                   args=(12341,)))
        self.assertEqual(response.status_code, 404)

    def test_category_with_entries(self):
        response = self.client.get(reverse('blog:category',
                                           args=(self.category.id,)))
        self.assertContains(response, self.category.name)
        self.assertQuerysetEqual(response.context['category'].entry_set.all(),
                                 ['<Entry: Entry Future>',
                                  '<Entry: Entry Past>'],)

    def test_empty_category(self):
        response = self.client.get(reverse('blog:category',
                                           args=(self.empty_category.id,)))
        self.assertContains(response, self.empty_category.name)
        self.assertQuerysetEqual(response.context['category'].entry_set.all(),
                                 [])
