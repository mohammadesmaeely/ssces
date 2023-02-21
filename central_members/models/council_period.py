from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class CouncilPeriod(BaseModel):
    period = models.CharField(
        max_length=150,
        verbose_name=_("period"),
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description"),
    )

    def __str__(self):
        return self.period

    class Meta:
        verbose_name = _("council period")
        verbose_name_plural = _("council period")
