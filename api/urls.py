from django.urls import path
from .views import PodcastList


urlpatterns = [
	path('podcasts/', PodcastList.as_view()),
]