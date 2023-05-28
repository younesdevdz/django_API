from django.db import models


#  -- Breakdown-- intervention



    

class Intervention  (models.Model):
    proactive = models.CharField(max_length=10)
    repor = models.CharField(max_length=150)
   

    
class Reporting(models.Model):
    proactive = models.CharField(max_length=50)
    proactive_remark = models.CharField(max_length=200)
 
class Breakdown (models.Model):
  
    tag = models.CharField(max_length=6)
    machine = models.CharField(max_length=20)
    dateTime = models.DateTimeField()
    report = models.ForeignKey(Reporting , on_delete= models.CASCADE , related_name="report" )
    
    
 
  