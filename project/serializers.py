# -*- coding: utf-8 -*-
from rest_framework import serializers
from project.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    field =
    class Meta:
        model = Article
