from rest_framework import serializers
from core.models.Podcast import Podcast
from core.models.Category import Category
from core.models.Author import Author


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name']

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['name']

class PodcastSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(read_only=True, many=True)
	authors = AuthorSerializer(read_only=True, many=True)
	
	class Meta:
		model = Podcast
		fields = ['title', 'description', 'authors', 'podcast_url', 'podcast_platform_url', 'image_url', 'categories']
