from django.conf.urls import patterns, url

from skeleton.apps.polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^login/$', views.login_user, name='login_user'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'polls/login.html'}),
    url(r'^logout/$', views.logout_view, name='logout_view'),
)
