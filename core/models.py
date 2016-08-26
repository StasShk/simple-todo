from __future__ import absolute_import, unicode_literals

from django.db import models

import datetime


import django.db.models.options as options

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description',)


class MainPage(Page):

    subpage_types = ['core.ItemList']

    search_fields = ()

    content_panels = [
        FieldPanel('title', classname="full title"),
    ]

    def get_context(self, request):
        # Get pages
        itemlists = ItemList.objects.child_of(self).live().order_by('-due_date')
        context = super(MainPage, self).get_context(request)
        context['itemlists'] = itemlists

        return context

    class Meta:
        description = "The homepage"
        verbose_name = "Main Page"


class ItemList(Page):
    ''
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True, )
    completed = models.BooleanField(default=None)
    completed_date = models.DateField(blank=True, null=True)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('due_date'),
        FieldPanel('completed'),
        FieldPanel('completed_date'),
        InlinePanel('item', label='Заявка')
    ]


class Item(Orderable):
    'Model for note'
    title = models.CharField(max_length=140)
    list = ParentalKey(ItemList, related_name='item')
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True, )
    completed = models.BooleanField(default=None)
    completed_date = models.DateField(blank=True, null=True)
    note = models.TextField(default='')
    priority = models.PositiveIntegerField(default=1)

    panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('due_date'),
        FieldPanel('completed'),
        FieldPanel('completed_date'),
        FieldPanel('note'),
        FieldPanel('priority'),
    ]

    # Has due date for an instance of this object passed?
    def overdue_status(self):
        "Returns whether the item's due date has passed or not."
        if self.due_date and datetime.date.today() > self.due_date:
            return 1

    def __str__(self):
        return self.title

    # Auto-set the item creation / completed date
    def save(self):
        # If Item is being marked complete, set the completed_date
        if self.completed:
            self.completed_date = datetime.datetime.now()
        super(Item, self).save()

    class Meta:
        ordering = ["priority"]
