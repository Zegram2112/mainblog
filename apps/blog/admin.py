from django.contrib import admin
from .models import Entry, Category, Tag


class EntryTaggingInline(admin.TabularInline):
    model = Tag.entries.through
    classes = ['collapse',]
    extra = 1


class EntryInline(admin.TabularInline):
    model = Entry
    classes = ['collapse',]
    extra = 0
    exclude = ('content',)


class EntryAdmin(admin.ModelAdmin):
    # List Presentation
    date_hierarchy = 'pub_date'
    list_display = ('title', 'category','pub_date')
    list_filter = ('pub_date', 'category__name')
    search_fields = ['category__name', 'title', 'content', 'tag__name']

    # Details Presentation
    inlines = [
        EntryTaggingInline,
    ]
    """fieldsets = [
        (None, {
            'fields': ['title', 'content']
        }),
        ("Date information", {
            'fields': ['pub_date']
        }),
    ]"""
    fields = (('title', 'category', 'pub_date'), 'content',)


class TagAdmin(admin.ModelAdmin):
    # List Presentation
    list_display = ('name',)
    search_fields = ('name',)

    # Details Presentation
    inlines = [
        EntryTaggingInline,
    ]
    exclude = ('entries',)


class CategoryAdmin(admin.ModelAdmin):
    # List Presentation
    list_display = ('name',)
    search_fields = ('name',)

    # Details Presentation
    inlines = [
        EntryInline
    ]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
