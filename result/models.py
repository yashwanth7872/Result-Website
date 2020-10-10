from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class  names(models.Model):
    reg_no = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.reg_no

class subject(models.Model):
    sub_code = models.CharField(max_length=6,primary_key=True)
    sub_short_form = models.CharField(max_length=5)
    sub_name = models.CharField(max_length=50)
    sub_credit = models.FloatField()
    def __str__(self):
        return self.sub_code

class marks(models.Model):
    reg_no = models.ForeignKey(names,on_delete=models.CASCADE)
    sub_code = models.ForeignKey(subject,on_delete=models.CASCADE)
    theory = models.IntegerField()
    internal = models.IntegerField()
    sem = models.IntegerField()
    class Meta:
        constraints = [
            models.UniqueConstraint(name='reg_no_sub_code',fields = ['reg_no','sub_code']),
        ]
    
    def __str__(self): 
        return str(self.reg_no)+ "-" +str(self.sub_code)



    

