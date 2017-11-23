from django.db import models
from djrichtextfield.models import RichTextField


class Entry(models.Model):
    """Class that represents a blog entry
    """
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publication date')
    content = RichTextField()
    category = models.ForeignKey('Category',
                                 on_delete=models.deletion.CASCADE)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    @staticmethod
    def search_entry(input):
        input = input.split()
        entry_list = Entry.objects.none()
        queries = []
        for word in input:
            by_title = Entry.objects.filter(title__icontains=word)
            by_tag = Entry.objects.filter(tag__name__icontains=word)
            by_category = Entry.objects.filter(category__name__icontains=word)
            queries.append(by_title)
            queries.append(by_tag)
            queries.append(by_category)
        return entry_list.union(*queries).order_by('-pub_date')


class Tag(models.Model):
    """Tag for marking blog entries"""
    name = models.CharField(max_length=45)
    entries = models.ManyToManyField(Entry)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Represents a category in which blog entries are enclosed"""
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name
