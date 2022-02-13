from django.db import models
from .Author import Author
from .Category import Category


class Podcast(models.Model):
	title = models.CharField('Title', max_length=300)
	description = models.TextField("Description")
	authors = models.ManyToManyField(Author, verbose_name='Authors')
	podcast_url = models.URLField('Podcast Url', max_length=1000)
	image_url = models.URLField('Image Url', max_length=2000)
	categories = models.ManyToManyField(Category, verbose_name="Categories")

	class Meta:
		verbose_name = "Podcast"
		verbose_name_plural = "Podcasts"

	def __str__(self):
		return self.title
