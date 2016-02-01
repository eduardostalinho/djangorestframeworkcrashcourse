# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from project.models import Article
from project.serializers import ArticleSerializer, UserSerializer

User = get_user_model()

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('users_view', request=request, format=format),
        'articles': reverse('articles_view', request=request, format=format)
    })


class ArticleListCreate(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(user=user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

user_view = UserView.as_view()
article_view = ArticleListCreate.as_view()
