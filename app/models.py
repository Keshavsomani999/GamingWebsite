
from django.db import models


# Create your models here.
class Games(models.Model):
    name=models.CharField(max_length=1111111)
    imageB=models.ImageField(upload_to='pics')
    imageA=models.ImageField(upload_to='pics')
    image1=models.ImageField(upload_to='pics')
    image2=models.ImageField(upload_to='pics')
    image3=models.ImageField(upload_to='pics')
    image4=models.ImageField(upload_to='pics')
    image5=models.ImageField(upload_to='pics')
    image6=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    desc=models.TextField(max_length=100000)
    typea=models.CharField(max_length=111111111)
    action=models.BooleanField(default=False)
    adventure=models.BooleanField(default=False)
    roleplay=models.BooleanField(default=False)
    Simulation=models.BooleanField(default=False)
    Sports=models.BooleanField(default=False)
    Strategy=models.BooleanField(default=False)
    free=models.BooleanField(default=False)
    top=models.BooleanField(default=False)
    logo=models.ImageField(upload_to='pics')
    download_link = models.URLField(max_length=50000)

    def __str__(self):
         return self.name
    class Meta:
        verbose_name_plural = "games"
        

class News(models.Model):
    name=models.CharField(max_length=1111)
    image1=models.ImageField(upload_to='pics')
    image2=models.ImageField(upload_to='pics')
    desc=models.TextField(max_length=100000)
    class Meta:
        verbose_name_plural = "news"
class Tranding(models.Model):
    image1=models.ImageField(upload_to='pics')
    image2=models.ImageField(upload_to='pics')
    image3=models.ImageField(upload_to='pics')
    image4=models.ImageField(upload_to='pics')
    image5=models.ImageField(upload_to='pics')
    name1=models.CharField(max_length=1111)
    name2=models.CharField(max_length=1111)
    name3=models.CharField(max_length=1111)
    name4=models.CharField(max_length=1111)
    name5=models.CharField(max_length=1111)
    
    class Meta:
        verbose_name_plural = "tranding"

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    message = models.TextField(max_length=11111)
    phone = models.IntegerField()
    games = models.CharField(max_length=111)
    price = models.IntegerField()
    download = models.URLField(max_length=500000)

    class Meta:
        verbose_name_plural = "orders"
    def str(self):
        return self.name