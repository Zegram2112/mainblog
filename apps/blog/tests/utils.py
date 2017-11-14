import datetime

from django.utils import timezone

from ..models import Entry, Tag, Category


def create_entry(name="Entry",
                 category_name="Category", text='',
                 days_from_now=0, pub_date=None):
    """Creates and saves an entry with determined values

    Parameters
    ----------
    name: str
        Title of the Entry
    category_name: str
        Title of the category Entry
    text: str
        Content of the Entry
    days_from_now: int
        Days of pub_date from now, negative to past
        and positive to future.
    pub_date: datetime
        If specified, it becomes the datetime of the entry
    Returns
    -------
    Entry
    """
    if pub_date is None:
        time = timezone.now() + datetime.timedelta(days=days_from_now)
    else:
        time = pub_date
    cat = Category(name=category_name)
    cat.save()
    return Entry.objects.create(
        title=name, category=cat, content=text, pub_date=time)


