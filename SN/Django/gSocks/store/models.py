from django.urls import reverse
from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=120)
    thickness = models.IntegerField()
    color = models.CharField(max_length=120)
    height = models.IntegerField()
    cost = models.DecimalField(max_digits=3, decimal_places=2)
    printed = models.CharField(max_length=120)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})