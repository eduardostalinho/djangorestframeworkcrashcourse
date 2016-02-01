# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.models import Article

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Article
