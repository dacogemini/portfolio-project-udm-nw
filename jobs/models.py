from django.db import models

# Pyhon needs to find the job model


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
