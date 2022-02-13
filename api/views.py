from rest_framework import viewsets
from .serializers import PodcastSerializer
from core.models.Podcast import Podcast
from rest_framework import generics


class PodcastList(generics.ListAPIView):
	"""
	Podcast View.
	"""
	serializer_class = PodcastSerializer
	
	def get_queryset(self):
		queryset = Podcast.objects.all()

		category = self.request.query_params.get("category")
		if category is not None:
			queryset = queryset.filter(categories__name=category)
		return queryset
