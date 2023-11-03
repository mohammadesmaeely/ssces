from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from library.models.book import Book
from users.models import User


class BookReserve(BaseModel):
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        verbose_name=_("book"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("user"),
    )

    reserve_date = models.DateField(
        verbose_name=_("reserve date")
    )

    has_been_returned = models.BooleanField(
        default=False,
        verbose_name=_("has been returned?")
    )

    class Meta:
        verbose_name = _("book reserve")
        verbose_name_plural = _("book reserves")

    def __str__(self):
        return f'{self.book} - {self.user}'
