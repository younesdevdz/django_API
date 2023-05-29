from django.db import models


#  -- Breakdown-- intervention



class ProductModel(models.Model):
        title =models.CharField(max_length=1000)
        price =models.IntegerField()
        category =models.CharField(max_length=1000)
        image = models.CharField(max_length=1000)






  
    

