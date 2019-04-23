from django.db import models

# Create your models here.
class Pool(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    field = models.URLField()
    account = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    info = models.TextField()

    class Meta:
        ordering = ('created',)