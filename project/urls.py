from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'project.views.api_root', name='api_root'),
    url(r'^users/$', 'project.views.user_view', name='users_view'),
    url(r'^articles/$', 'project.views.article_view', name='articles_view'),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token')
)
