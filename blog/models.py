from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


PUBLISH_CHOICES = [
('draft','Draft'),
('publish', 'Publish'),
('private','Private')
]

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
       def get_queryset(self):
           return super(PublishedManager,
                        self).get_queryset()\
                             .filter(status='publish')

class Blog(models.Model):
	title = models.CharField(max_length=250, null = False)
	description = models.CharField(max_length=200)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	authors = models.ManyToManyField(Author)
	body = models.TextField	()
	publish = models.DateTimeField(auto_now=False,default = timezone.now,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=120, choices = PUBLISH_CHOICES, default='draft')
	objects = models.Manager()
	published = PublishedManager()
	
	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		"""
		Returns the url to access a detail record for this blog.
		"""
		return reverse('blog-detail', args=[str(self.id)])

# class Author(models.Model):
# 	firstname = models.CharField(max_length=150,null = False)
# 	lastname = models.CharField(max_length=150,null = False)

	
