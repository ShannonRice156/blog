from django.db import models
from users.models import UserProfile
import uuid

# Create your models here.


class Blog(models.Model):
    owner = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=100)
    featured_image = models.ImageField(
        null=False, blank=False, default="default.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
