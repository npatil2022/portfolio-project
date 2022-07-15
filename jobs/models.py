from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.summary


class Job_ac(models.Model):
    image = models.ImageField(upload_to='')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.summary

