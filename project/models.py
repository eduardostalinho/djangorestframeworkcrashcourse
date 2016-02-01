# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email


class Article(models.Model):
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
