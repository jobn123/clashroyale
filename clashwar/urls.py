from django.conf.urls import url
from .views import CreateArenaCardsView
from .views import CreatePopularCardsView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^arenaCardslists/$', CreateArenaCardsView.as_view(), name="ArenaCards"),
    url(r'^popularCardslists/$', CreatePopularCardsView.as_view(), name="PopularCards"),
]

urlpatterns = format_suffix_patterns(urlpatterns)