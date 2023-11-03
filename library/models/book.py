from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Book(BaseModel):
    name = models.CharField(
        max_length=256,
        verbose_name=_("name")
    )

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.name
