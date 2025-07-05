from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    question = models.CharField(
        max_length=128,
        verbose_name=_("Question")
    )
    answer = models.TextField(
        verbose_name=_("Answer")
    )

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question
