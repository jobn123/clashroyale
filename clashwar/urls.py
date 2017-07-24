from django.conf.urls import url
from .views import CreateArenaCardsView
from .views import CreatePopularCardsView
from .views import CreateDecksView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^arenaCardslists/$', CreateArenaCardsView.as_view(), name="ArenaCards"),
    url(r'^popularCardslists/$', CreatePopularCardsView.as_view(), name="PopularCards"),
    url(r'^decklists/$', CreateDecksView.as_view(), name="Decks"),
]

urlpatterns = format_suffix_patterns(urlpatterns)