from django.conf.urls   import url
from .                  import views


# Required when multiple apps are present in the project:
# used by <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li> in index.htnl to resolve the application name
app_name = "polls"

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
