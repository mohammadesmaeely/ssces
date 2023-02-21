from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    history = HistoricalRecords(inherit=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at")
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name='آیا حذف شده است؟'
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
