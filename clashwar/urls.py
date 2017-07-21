from django.conf.urls import url
from .views import CreateArenaCardsView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^arenaCardslists/$', CreateArenaCardsView.as_view(), name="ArenaCards"),
]

urlpatterns = format_suffix_patterns(urlpatterns)