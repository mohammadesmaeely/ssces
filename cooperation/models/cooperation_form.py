from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class CooperationForm(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("title"),
        unique=True,
    )

    description = models.TextField(
        verbose_name=_("description"),
    )

    show_on_site = models.BooleanField(
        default=True,
        verbose_name=_("show on site?"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("cooperation form")
        verbose_name_plural = _("cooperation forms")
