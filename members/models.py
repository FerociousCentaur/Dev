from django.db import models

# Create your models here.



class member(models.Model):
    quote = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    contact = models.EmailField(max_length=30)
    image = models.ImageField(blank=True, upload_to="gallery")
    superiority = models.IntegerField(null=True)
    number = models.IntegerField(null=True)


    def __str__(self):
        return self.name

class rovers(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    image1 = models.ImageField(null=True, upload_to="rov")
    image2 = models.ImageField(null=True, upload_to="rov")
    image3 = models.ImageField(null=True, upload_to="rov")
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.name