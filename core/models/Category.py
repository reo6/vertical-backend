from django.db import models


class Category(models.Model):
	name = models.CharField('Name', max_length=250)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"