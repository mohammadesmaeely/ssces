from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from events.models.event import Event
from users.models import User

phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$',message="Phone number is invalid")


class RegisteredEvent(BaseModel):
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        verbose_name=_("event"),
        related_name='registered_events',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("user"),
        related_name='registered_events',
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[phone_regex]
    )

    is_paid = models.BooleanField(
        default=False,
        verbose_name=_("is paid?")
    )

    class Meta:
        verbose_name = _("registered event")
        verbose_name_plural = _("registered events")
        unique_together = ['event', 'phone_number']

    def __str__(self):
        if self.user:
            return f'{self.event} - {self.user}'
        return f'{self.event} - {self.phone_number}'
