from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from events.models.event_category import EventCategory


class Event(BaseModel):
    category = models.ForeignKey(
        EventCategory,
        on_delete=models.PROTECT,
        related_name='events',
        verbose_name=_("event category"),
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_("title"),
    )

    description = models.TextField(
        verbose_name=_("description"),
    )

    registration_fee = models.IntegerField(
        default=0,
        verbose_name=_("registration fee"),
    )

    date = models.DateField(
        verbose_name=_("event date"),
    )

    authenticated_user_capacity = models.IntegerField(
        verbose_name=_("authenticated user capacity"),
        help_text=_("if it runs out, authenticate user use anonymous user capacity")
    )

    authenticated_user_price = models.IntegerField(
        verbose_name=_("authenticated user price"),
    )

    anonymous_user_capacity = models.IntegerField(
        verbose_name=_("anonymous user capacity"),
    )

    anonymous_user_price = models.IntegerField(
        verbose_name=_("anonymous user price"),
    )

    show_on_site = models.BooleanField(
        default=True,
        verbose_name=_("show on site?"),
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.title
