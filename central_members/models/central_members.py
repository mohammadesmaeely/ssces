from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from central_members.models.council_period import CouncilPeriod
from core.models import BaseModel
from users.models import User

phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$', message="Phone number is invalid")

class CentralMember(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("user")
    )

    name = models.CharField(
        max_length=150,
        verbose_name=_("name")
    )

    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("image"),
    )

    council = models.ForeignKey(
        CouncilPeriod,
        on_delete=models.PROTECT,
        verbose_name=("council period"),
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

    telegram_address = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("telegram address"),
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description")
    )

    def __str__(self):
        return f'{self.name} - {self.council}'

    class Meta:
        verbose_name = _("central member")
        verbose_name_plural = _("central members")
        unique_together = ['user', 'council']
