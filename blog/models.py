from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100)
    feature_img = models.ImageField(blank=True, upload_to='feature_pics')
    excerpt = RichTextField(default='')
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
