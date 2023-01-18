from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=15)
    pid=models.IntegerField()
    category=models.CharField(max_length=15)
    categoryid=models.IntegerField()

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
