from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class GalleryImage(BaseModel):
    image = models.ImageField(
        verbose_name=_("image"),
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description"),
    )

    class Meta:
        verbose_name = _("gallery image")
        verbose_name_plural = _("gallery images")
