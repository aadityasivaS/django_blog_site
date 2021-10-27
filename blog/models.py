from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    STATUS_OPTIONS = (
        ('DR', 'Draft'),
        ('PB', 'Published')
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_OPTIONS)
    created_on = models.DateTimeField()

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    