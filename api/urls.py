from django.urls import path
from .views import PodcastList, CategoryList


urlpatterns = [
	path('podcasts/', PodcastList.as_view()),
	path('categories/', CategoryList.as_view()),
]