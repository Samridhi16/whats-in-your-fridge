from django.db import models

class AddModel(models.Model):

    #items to be added to the fridge
    description = models.CharField(max_length=20,default='',null=False)
    objectHandler = models.Manager()