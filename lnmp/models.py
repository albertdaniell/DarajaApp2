from django.db import models

# Create your models here.


class LipaNaMpesa(models.Model):
    checkoutRequestID= models.CharField(max_length=50,blank=True, default='')
    merchantRequestID= models.CharField(max_length=50,blank=True, default='')
    resultCode=models.IntegerField(null=True)
    resultDesc= models.CharField(max_length=50,blank=True, default='')
    amount=models.FloatField(null=True, blank=True, default=None)
    mpesaReceiptNumber=models.CharField(max_length=50,blank=True, null=True)
    transactionDate=models.DateTimeField(auto_now=False, auto_now_add=False)
    phoneNumber= models.CharField(max_length=15,blank=True, null=True)

   
 


