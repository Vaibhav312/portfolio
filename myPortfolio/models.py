from django.db import models


# Create your models here.


class ContactUsInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name