from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class EventCategory(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name=_('category name')
    )

    ordering_in_list = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("ordering in list")
    )

    class Meta:
        verbose_name = _("event category")
        verbose_name_plural = _("event categories")
        ordering = ['ordering_in_list']

    def __str__(self):
        return self.name
