# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
