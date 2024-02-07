from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFT = 'DF', 'Draft'

    title = models.CharField(max_length=200, help_text="Post title.")
    slug = models.SlugField(max_length=200, unique_for_date='publish',
                            help_text="The slug of the post.")
    snippet = models.CharField(max_length=250,default="No snippet", help_text="The snippet of the post.")
    body = CKEditor5Field('content', config_name='extends')
    publish = models.DateTimeField(default=timezone.now,
                                   help_text="The date and time the post was published.")
    created_date = models.DateTimeField(auto_now_add=True,
                                        help_text="The date and time the post was created.")
    updated_date = models.DateTimeField(auto_now=True, help_text="The date and time the post was edited.")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default=Status.DRAFT, max_length=20,
                              choices=Status.choices)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


