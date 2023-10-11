from django.db import models
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=256)
    comment = models.TextField()
    price = models.IntegerField()
    performance = models.TextField()
    display = models.TextField()
    camera = models.TextField()
    battery = models.TextField()
    image1 = models.TextField()
    image2 = models.TextField()

    def get_absolute_url(self):
        return reverse("item_single",args=[self.name])

    def __str__(self):
        return self.name
