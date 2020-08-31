from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=250)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("page-detail", kwargs={"page_id": self.id})
