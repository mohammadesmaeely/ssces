from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from cooperation.models.cooperation_form import CooperationForm
from users.models import User

phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$', message="Phone number is invalid")


class CooperationReply(BaseModel):
    cooperation = models.ForeignKey(
        CooperationForm,
        on_delete=models.PROTECT,
        verbose_name=_("cooperation"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
    )

    text = models.TextField(
        verbose_name=_("text"),
    )


    phone_number = models.CharField(
        max_length=13,
        null=True,
        blank=True,
        validators=[phone_regex],
        verbose_name=_("phone number"),
    )

    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name=_("email"),
    )

    def __str__(self):
        return f'{self.cooperation} - {self.user}'

    class Meta:
        verbose_name = _("cooperation reply")
        verbose_name_plural = _("cooperation replies")
        unique_together = ['cooperation', 'user']
