from django.db import models


# Create your models here.


class ContactUsInfo(models.Model):
    name=models.CharField(max_length=50,error_messages={'required': 'Please enter your name'})
    email=models.EmailField(error_messages={'required': 'Please enter valid email'})
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name